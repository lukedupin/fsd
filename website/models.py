from django.db import models

# Create your models here.
class Location(models.Model):
  id = models.AutoField(primary_key=True)
  ip_address = models.CharField(max_length=32)
  lat = models.DecimalField(max_digits=14,decimal_places=10)
  lng = models.DecimalField(max_digits=14,decimal_places=10)

class Tracker(models.Model):
  id = models.AutoField(primary_key=True)
  location = models.ForeignKey(Location)
  path = models.CharField(max_length=128)
