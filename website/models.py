from django.db import models

# Create your models here.
class Location(models.Model):
  id = models.AutoField(primary_key=True)
  ip_address = models.CharField(max_length=32)
  lat = models.DecimalField(max_digits=14,decimal_places=10)
  lng = models.DecimalField(max_digits=14,decimal_places=10)
  city = models.CharField(max_length=128)
  region = models.CharField(max_length=128)

  def __unicode__(self):
    count = 0
    for tracker in self.tracker_set.all():
      count += tracker.count
    return self.city +", "+ self.region +" ("+ str(count) +")"

class Tracker(models.Model):
  id = models.AutoField(primary_key=True)
  location = models.ForeignKey(Location)
  path = models.CharField(max_length=128)
  count = models.IntegerField()
  created_on = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.path + " ("+ str(self.count) +") - "+ \
           self.location.__unicode__()

class AndroidBug(models.Model):
  id = models.AutoField(primary_key=True)
  package_name = models.CharField(max_length=128)
  package_version = models.CharField(max_length=128)
  stacktrace = models.TextField(max_length=32768)
  created_on = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.package_name +" - "+ str(self.created_on)
