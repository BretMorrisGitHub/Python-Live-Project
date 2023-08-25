from django.forms import ModelForm
from .models import Location, Flights


# Creates Location Form based on the Location Model
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class detailsForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class FlightsForm(ModelForm):
    class Meta:
        model = Flights
        fields = '__all__'
