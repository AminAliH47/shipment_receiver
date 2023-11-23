from rest_framework.generics import ListAPIView
from shipments import models, serializers, filters


class ShipmentsListView(ListAPIView):
    queryset = (
        models.Shipments.objects.
        prefetch_related('articles').
        filter(is_deleted=False)
    )
    serializer_class = serializers.ShipmentsSerializer
    filterset_class = filters.ShipmentFilters
