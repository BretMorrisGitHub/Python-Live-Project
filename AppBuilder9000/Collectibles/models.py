from django.db import models

# Create the Card Model
class Cards(models.Model):    # Card Categories
    Category_Choices = [
        ('Pokemon', 'Pokemon'),
        ('Magic', 'Magic'),
        ('Soccer', 'Soccer'),
        ('Baseball', 'Baseball'),
        ('Basketball', 'Basketball'),
        ('Football', 'Football'),
    ]

    # Model Fields
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category_Choices)
    year = models.IntegerField()
    set = models.CharField(max_length=50)
    description = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.name

