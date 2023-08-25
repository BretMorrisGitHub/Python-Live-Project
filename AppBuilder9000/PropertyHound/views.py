from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropertyForm
from .models import Property
import requests
import json

# Adds function to views to render home page
def prophound_home(request):
    return render(request, 'PropertyHound/PropHound_home.html')


# Function to render Add New Listing page when requested
def prophound_create(request):
    form = PropertyForm(data=request.POST or None) # Retrieve the Property Form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): # Checks to see if the submitted form is valid, and saves the form if true
            form.save() # Saves new listing
            return redirect('prophound_home') # Returns user back to home page
    content = {'form': form} # Saves content to template as dictionary
    # adds content of form to page
    return render(request, 'PropertyHound/PropHound_create.html', content)

# Function will render Current Listings page when requested
def prophound_read(request):
    property = Property.Properties.all()
    content = {'property': property}
    return render(request, 'PropertyHound/PropHound_read.html', content)


# Function will render the details page with info for specific listing selected
def prophound_details(request, pk):
    property = get_object_or_404(Property, pk=pk)
    content = {'property': property}
    return render(request, 'PropertyHound/PropHound_details.html', content)

def prophound_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    form = PropertyForm(data=request.POST or None, instance=property)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'property': property}
    return render(request, 'PropertyHound/PropHound_edit.html', content)


def prophound_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('../../read')
    content = {'property': property}
    return render(request, 'PropertyHound/PropHound_delete.html', content)

def prophound_api(request):
    url = "https://api.wheretheiss.at/v1/satellites/25544"

    querystring = {"units": "miles"}

    headers = {}

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    latitude = api_info["latitude"]
    longitude = api_info["longitude"]
    content = {"location": str(latitude) + ',' + str(longitude)}
    return render(request, 'PropertyHound/PropHound_api.html', content)
