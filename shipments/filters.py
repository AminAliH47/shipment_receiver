import django_filters as filters
from shipments import models


class ShipmentFilters(filters.FilterSet):
    carrier = filters.CharFilter(
        field_name='carrier__name',
        lookup_expr='exact',
    )

    class Meta:
        model = models.Shipments
        fields = ('tracking_number', 'carrier')
