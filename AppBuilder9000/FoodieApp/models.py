from django.db import models

# creates model for users to add recipes
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50, default="", blank=True, null=False)
    created_by = models.CharField(max_length=150, default="", blank=True, null=False)
    ingredients = models.CharField(max_length=100, default="", blank=True, null=False)
    directions = models.TextField(max_length=300, default="", blank=True, null=False)


    objects = models.Manager()

    def __str__(self):
        return self.recipe_name
