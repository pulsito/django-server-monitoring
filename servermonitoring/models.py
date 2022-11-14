from datetime import datetime
from django.db import models


# Create your models here.
class ServerMonitoring(models.Model):
    server_name = models.CharField(max_length=50, blank=False)
    notification_time = models.TimeField(default=datetime.now, blank=False)
    notification_type = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    servers_group = models.IntegerField(default=0)
    servers_group_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=False)
