# -*- coding: utf-8 -*-

import contextlib
import os
import time
from fabric.api import cd, env, roles, run, settings

env.root = os.path.dirname(__file__)
env.app = os.path.join(env.root, 'manouche_us')
env.project_root = '/home/manouche/djangodash2011'
env.app_root = os.path.join(env.project_root, 'manouche_us')
env.virtualenv_dir = '/home/manouche/.virtualenvs/manouche'
env.user = 'manouche'
env.roledefs = {
    'server' : ['manouche.us'],
}

@roles('server')
def update_app():
    with cd(env.project_root):
        run("git pull origin master")

@roles('server')
def collect_static_files():
    with cd(env.project_root):
        run("%(virtualenv_dir)s/bin/python manage.py collectstatic -v 0 --noinput")

@roles('server')
def pip_install():
    run("%(virtualenv_dir)s/bin/pip install -r %(project_root)s/requirements_env.txt" % env)

@roles('server')
def start_gunicorn():
    with cd(env.app_root):
        run("%(virtualenv_dir)s/bin/gunicorn_django -p gunicorn.pid --daemon --workers=4" % env)

@roles('server')
def stop_gunicorn():
    with contextlib.nested(cd(env.app_root), settings(warn_only=True)):
        run("kill -9 `cat gunicorn.pid`")

@roles('server')
def stop_nginx():
    run("sudo service nginx stop")

@roles('server')
def start_nginx():
    run("sudo service nginx start")

@roles('server')
def restart_nginx():
    stop_nginx()
    start_nginx()

@roles('server')
def restart_gunicorn():
    stop_gunicorn()
    time.sleep(10)
    start_gunicorn()

@roles('server')
def syncdb():
    with cd(env.app_root):
        run("%(virtualenv_dir)s/bin/python manage.py syncdb --noinput && %(virtualenv_dir)s/bin/python manage.py createsuperuser --username=admin --email=admin@admin.com" % env)

@roles('server')
def deploy():
    update_app()
    pip_install()
    collect_static_files()
    restart_gunicorn()
    restart_nginx()
