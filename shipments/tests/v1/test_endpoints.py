from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestShipments(TestCase):
    SHIPMENTS_LIST_URL = reverse('shipments:shipments:list')

    def test_shipments_list_response_200(self):
        response = self.client.get(self.SHIPMENTS_LIST_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
