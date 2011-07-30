from django.utils import unittest
from django.test import RequestFactory, Client

from project.views import index


class TestViews(unittest.TestCase):
    def test_index_view(self):
        request_factory = RequestFactory()
        request = request_factory.post("/")
        response = index(request)

        self.assertEquals(response.context_data.keys(), ['form'])

    def test_error_when_url_is_not_github(self):
        url = "http://foo.com"
        client = Client()
        response = client.post("/", {"url": url})

        form_erros = response.context[0].get('form').errors
        self.assertEquals(form_erros, {'url': [u"Url should be from github.com! I\'m a fanboy :D"]})

