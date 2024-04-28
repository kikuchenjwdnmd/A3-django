from django.db import models


class Users(models.Model):
    id = models.AutoField('user_id', primary_key=True)
    email = models.EmailField('email', max_length=100, null=False, unique=True)
    username = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=32, null=False)
    age = models.IntegerField(null=False)


class Flights(models.Model):
    flightNo = models.CharField(max_length=10)
    departure = models.CharField(max_length=5)
    departureCityName = models.CharField(max_length=50)
    departureFullName = models.CharField(max_length=100)
    arrive = models.CharField(max_length=5)
    arriveCityName = models.CharField(max_length=50)
    arriveFullName = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=4)
    operated = models.CharField(max_length=100)
    airlines = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=200)
    aircraft = models.CharField(max_length=50)
    luggageFree = models.CharField(max_length=10)
    flightTime = models.CharField(max_length=10)
    nonStop = models.BooleanField()
