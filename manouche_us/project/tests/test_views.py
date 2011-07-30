from django.utils import unittest
from django.test import RequestFactory, Client

from project.views import index


class TestViews(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        request_factory = RequestFactory()
        request = request_factory.post("/")
        response = index(request)

        self.assertEquals(response.context_data.keys(), ['form'])

    def test_error_when_url_is_not_github(self):
        url = "http://foo.com"
        response = self.client.post("/", {"url": url})

        form_erros = response.context[0].get('form').errors
        self.assertEquals(form_erros, {'url': [u"Url should be from github.com! I\'m a fanboy :D"]})

    def test_submit_a_project(self):
        url = 'http://github.com/tarsis/'
        response = self.client.post('/', {"url": url})

        location = response.items()[1]
        self.assertEquals(302, response.status_code)
        self.assertEquals(('Location', 'http://testserver/wait/'), location)

