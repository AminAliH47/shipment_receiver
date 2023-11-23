from django.db import models

from common.models import AbstractModel


class ShipmentStatus(models.TextChoices):
    IN_TRANSIT = 'in-transit'
    INBOUND_SCAN = 'inbound-scan'
    DELIVERY = 'delivery'
    TRANSIT = 'transit'
    SCANNED = 'scanned'


class Shipments(AbstractModel):
    tracking_number = models.CharField(max_length=10)
    carrier = models.ForeignKey(
        to='shipments.carriers',
        on_delete=models.CASCADE,
        related_name='carrier'
    )
    sender_address = models.TextField()
    receiver_address = models.TextField()
    articles = models.ManyToManyField(
        to='articles.Articles',
        related_name='articles',
    )
    status = models.CharField(max_length=12, choices=ShipmentStatus.choices)

    class Meta:
        db_table = 'shipments'
        unique_together = ('tracking_number', 'carrier')

    def __str__(self) -> str:
        return f'{self.tracking_number} - {self.carrier}'


class Carriers(AbstractModel):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'carriers'

    def __str__(self) -> str:
        return self.name
