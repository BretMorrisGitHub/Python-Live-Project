from django.db import models

TYPE_CHOICES = {
    ('Amusement Park', 'Amusement Park'),
    ('Art', 'Art'),
    ('Historic', 'Historic'),
    ('Nature/Scenic', 'Nature/Scenic'),
}

CITY_CHOICES = {
    ('Aarhus', 'Aarhus'),
    ('Billund', 'Billund'),
    ('Copenhagen', 'Copenhagen'),
    ('Faroe Islands', 'Faroe Islands'),
    ('Odense', 'Odense'),
    ('Skagen', 'Skagen'),
    ('Vejle', 'Vejle'),
}

DESTINATION_CHOICES = {
    ('AAL', 'AAL'),
    ('AAR', 'AAR'),
    ('BLL', 'BLL'),
    ('CPH', 'CPH'),
    ('RKE', 'RKE'),
    ('ODE', 'ODE'),
    ('FAE', 'FAE')

}


class Location(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    city = models.CharField(max_length=60, choices=CITY_CHOICES)
    description = models.TextField(max_length=350, default="", blank=True)
    image = models.CharField(max_length=255, default='', blank=True)

    Locations = models.Manager()

    def __str__(self):
        return self.name


class Flights(models.Model):
    origin = models.CharField(max_length=6, default="JFK", blank=True, null=False)
    destination = models.CharField(max_length=6, choices=DESTINATION_CHOICES)
    date = models.DateField(max_length=12, default="YYYY-MM-DD", blank=True)
    returnDate = models.DateField(max_length=12, default="YYYY-MM-DD", blank=True)

    Flights = models.Manager()

    def __str__(self):
        return self.destination
