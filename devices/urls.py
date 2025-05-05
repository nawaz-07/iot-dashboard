from django.urls import path
from .views.devices_views import device_detail, device_list
from .views.user_views import register_user, login_user

urlpatterns = [
    path('devices/',device_list, name='device-list'),
    path('devices/<int:pk>/',device_detail, name='device-detail'),
    path('register/', register_user, name='register-user'),
    path('login/', login_user, name='login-user'),
]