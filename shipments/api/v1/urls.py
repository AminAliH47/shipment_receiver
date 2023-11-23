from django.urls import path
from shipments.api.v1 import views

app_name = 'shipments'

urlpatterns = (
    path('shipments/', views.ShipmentsListView.as_view(), name='list'),
)
