from django.test import TestCase
from model_bakery import baker
from rest_framework.test import APIClient


class CollectionFrequencyTestCase(TestCase):

    def setUp(self):
        self.op_bin = baker.make('Operation', _quantity=10)
        self.client = APIClient()

    def test_collection_frequency(self):
        response = self.client.get('/collection-frequency/')
        self.assertEqual(len(response.data), 10)
        print(response.data)