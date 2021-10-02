from django.db import models

class Store(models.Model):
    #Store Logistics
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=50)
    hoursOfOperation = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    store = models.ManyToManyField(Store)
