import django_filters as filters
from shipments import models


class ShipmentFilters(filters.FilterSet):
    class Meta:
        model = models.Shipments
        fields = ('tracking_number', 'carrier')
