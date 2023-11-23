from django.test import TestCase
from shipments import models
from articles.models import Articles


class TestShipmentModels(TestCase):
    def _sample_article(self):
        return Articles.objects.create(
            sku='test',
            name='test',
            price=100,
            quantity=1,
        )

    def _sample_carries(self):
        return models.Carriers.objects.create(name='test')

    def test_shipment_create(self):
        article = self._sample_article()

        shipment = models.Shipments(
            tracking_number='test',
            carrier=self._sample_carries(),
            sender_address='test',
            receiver_address='test',
            status='test',
        )
        shipment.save()
        shipment.articles.set([article])

        shipment_count = models.Shipments.objects.count()

        self.assertEqual(shipment_count, 1)
