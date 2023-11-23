from rest_framework.generics import ListAPIView
from shipments import models, serializers
from shipments.filters import ShipmentFilters
import django_filters.rest_framework as filters


class ShipmentsListView(ListAPIView):
    queryset = (
        models.Shipments.objects.
        prefetch_related('articles').
        filter(is_deleted=False)
    )
    serializer_class = serializers.ShipmentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShipmentFilters
