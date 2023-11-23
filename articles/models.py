from django.db import models

from common.models import AbstractModel


class Articles(AbstractModel):
    sku = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'articles'

    def __str__(self) -> str:
        return f'{self.sku} - {self.name}'
