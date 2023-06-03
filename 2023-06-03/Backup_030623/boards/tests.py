from django.test import TestCase

# Create your tests here.
#from django.core.urlresolvers import reverse deprecated in Django 2.0
from django.urls import reverse


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('listboards')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
