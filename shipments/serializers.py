from rest_framework import serializers

from shipments.models import Shipments
from articles.serializers import ArticlesSerializer
from shipments.utils import get_data_from_weather_api


class ShipmentsSerializer(serializers.ModelSerializer):
    carrier = serializers.StringRelatedField()
    articles = ArticlesSerializer(many=True)
    weather = serializers.SerializerMethodField()

    def get_weather(self, obj):
        city = str(obj.receiver_address).split(' ')[3][:-1]

        return get_data_from_weather_api(city)

    class Meta:
        model = Shipments
        fields = (
            'tracking_number', 'carrier',
            'sender_address', 'receiver_address',
            'articles', 'status', 'weather',
        )
