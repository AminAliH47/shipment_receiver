from django.contrib import admin
from shipments import models

admin.site.register(models.Shipments)
admin.site.register(models.Carriers)
