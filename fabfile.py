# -*- coding: utf-8 -*-

import contextlib
import os
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
def pip_install():
    run("%(virtualenv_dir)s/bin/pip install -r %(project_root)s/requirements_env.txt" % env)

@roles('server')
def _start_gunicorn():
    with cd(env.app_root):
        run("/etc/init.d/gunicorn-manouche start")

@roles('server')
def _stop_gunicorn():
    with contextlib.nested(cd(env.app_root), settings(warn_only=True)):
        run("/etc/init.d/gunicorn-manouche stop")

@roles('server')
def restart_gunicorn():
    _stop_gunicorn()
    _start_gunicorn()

@roles('server')
def deploy():
    update_app()
    pip_install()
    restart_gunicorn()
