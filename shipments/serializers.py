from rest_framework import serializers

from shipments.models import Shipments
from articles.serializers import ArticlesSerializer
from shipments.utils import get_data_from_weather_api


class ShipmentsSerializer(serializers.ModelSerializer):
    articles = ArticlesSerializer(many=True)
    weather = serializers.SerializerMethodField()

    def get_weather(self, obj):
        print(obj.receiver_address)

        return get_data_from_weather_api('Paris')

    class Meta:
        model = Shipments
        fields = (
            'tracking_number', 'carrier',
            'sender_address', 'receiver_address',
            'articles', 'status', 'weather',
        )
