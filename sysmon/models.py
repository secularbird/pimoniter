from django.db import models


# Create your models here.
class SystemMonitor(models.Model):
    cpu_precentage = models.FloatField()
    local_weather_temp = models.FloatField()
    sensor_temp = models.FloatField()
    datetime = models.DateField()
