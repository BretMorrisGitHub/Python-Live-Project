from django.contrib import admin

# register model
from .models import Recipe

admin.site.register(Recipe)
