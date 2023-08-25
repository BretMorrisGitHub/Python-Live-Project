from django.db import models
from django import forms


# Creates the Property Model
class Property(models.Model):
    street_add = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField(max_length=5)
    price_listed = models.DecimalField(max_digits=15, decimal_places=2)
    date_listed = models.DateField()
    loan_type = models.CharField(max_length=3)

    # Defines the model manager for Properties
    Properties = models.Manager()

    # Referencing a specific property will return the street address not the primary key
    def __str__(self):
        return self.street_add


class LocationMoment(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()

    LocationMoments = models.Manager()

    def __str__(self):
        return self.longitude
        return self.latitude