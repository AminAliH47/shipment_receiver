from rest_framework import serializers

from articles import models


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Articles
        fields = ('sku', 'name', 'price', 'quantity')
