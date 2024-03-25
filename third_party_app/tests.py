from django.test import TestCase
from unittest.mock import patch
from rest_framework.test import APIClient
# Create your tests here.

class NounProjectTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_pokeball_img(self, mock_get):
        ball = 'pokeball'


