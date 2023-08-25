from django import forms
from .models import Cards

class CardsForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ('name', 'category', 'year', 'set', 'description')
        widgets = {}