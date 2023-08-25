from django.forms import ModelForm
from .models import Property


# Creates Property Form based on Property Model
class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
