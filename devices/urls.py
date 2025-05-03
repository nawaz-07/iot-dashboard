from django.urls import path
from .views import device_detail, device_list

urlpatterns = [
    path('devices/',device_list, name='device-list'),
    path('devices/<int:pk>/',device_detail, name='device-detail'),
]