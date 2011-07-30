from django.utils import unittest
from django.test import RequestFactory

from project.views import index


class TestViews(unittest.TestCase):
    def test_index_view(self):
        request_factory = RequestFactory()
        request = request_factory.post("/")
        response = index(request)

        self.assertEquals(response.context_data.keys(), ['form'])
