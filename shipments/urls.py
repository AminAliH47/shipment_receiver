from django.urls import path, include

app_name = 'shipments'

urlpatterns = (
    path('v1/', include('shipments.api.v1.urls')),
)
