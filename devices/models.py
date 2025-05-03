from django.db import models

class Device(models.Model):
    DEVICE_TYPES = [
        ('sensor','SENSOR'),
        ('actuator','ACTUATOR'),
        ('switch','SWITCH'),
    ]

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=20,choices=DEVICE_TYPES)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.device_type})"
