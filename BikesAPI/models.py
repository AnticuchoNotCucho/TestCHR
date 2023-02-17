from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Location(models.Model):
    city: models.CharField(max_length=50)
    country: models.CharField(max_length=50)
    latitude: models.FloatField()
    longitude: models.FloatField()


class Network(models.Model):
    company = models.JSONField()
    gbfs_href = models.CharField(max_length=50)
    href = models.CharField(max_length=50)
    id = models.CharField(primary_key=True, max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Station(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    timestamp = models.DateTimeField()
    extra = models.ForeignKey('Extra', on_delete=models.CASCADE)


class Extra(models.Model):
    address = models.CharField(max_length=200)
    altitude = models.FloatField()
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.BigIntegerField()
    normal_bikes = models.IntegerField()
    payment = models.JSONField()
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=10)
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=100)
