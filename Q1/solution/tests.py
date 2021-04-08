from django.test import TestCase, client
from model_bakery import baker
from datetime import datetime, timedelta
from rest_framework.test import APIClient


class LastPointTestCase(TestCase):

    def setUp(self):
        self.valid_date_1 = datetime.now() - timedelta(hours=15)
        self.valid_date_2 = datetime.now() - timedelta(hours=47)
        self.invalid_date_1 = datetime.now() - timedelta(hours=49)
        self.nav_rec_1 = baker.make('NavigationRecord',
            datetime=self.valid_date_1)
        self.nav_rec_2 = baker.make('NavigationRecord',
            datetime=self.valid_date_2)
        self.nav_rec_3 = baker.make('NavigationRecord',
            datetime=self.valid_date_2)
        self.nav_rec_4 = baker.make('NavigationRecord',
            datetime=self.invalid_date_1)
        self.nav_rec_5 = baker.make('NavigationRecord',
            datetime=self.invalid_date_1)
        self.client = APIClient()

    def test_last_point_list(self):
        response = self.client.get('/last-points/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_cached_last_point_list(self):
        response = self.client.get('/last-points/')
        last_modified = response.headers["Last-Modified"]

        res1 = self.client.get('/last-points/', HTTP_IF_MODIFIED_SINCE=last_modified)
        self.assertEqual(res1.status_code, 304)

    