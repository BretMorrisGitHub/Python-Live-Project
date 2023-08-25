from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocationForm, detailsForm, FlightsForm
from .models import Location
import requests
from bs4 import BeautifulSoup


# Create your views here.
#   This function will render the Home page when requested
def DanishTourism_home(request):
    return render(request, 'home/DanishTourism_home.html')


# This function will render the Add Location page when requested
def add_location(request):
    # Retrieves the Location form
    form = LocationForm(data=request.POST or None)
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Checks to see if the submitted form is valid
            form.save()  # Saves the new location
            return redirect('DanishTourism_Locations')  # Returns to location page
    content = {'form': form}  # Saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'DanishTourism_AddLocation.html', content)


def displayLocations(request):
    locations = Location.Locations.all()
    content = {'locations': locations}
    return render(request, 'DanishTourism_Locations.html', content)


def displayDetails(request, pk):
    pk = int(pk)
    item = get_object_or_404(Location, pk=pk)
    return render(request, 'DanishTourism_ViewDetails.html', {'item': item})


def udDetails(request, pk):
    pk = int(pk)
    item = get_object_or_404(Location, pk=pk)
    form = detailsForm(data=request.POST or None, instance=item)
    content = {'form': form, 'item': item}
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('DanishTourism_Locations')
        else:
            print(form.errors)
    else:
        return render(request, 'DanishTourism_Edit.html', content)


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('DanishTourism_Locations')
    context = {'item': item,}
    return render(request, "DanishTourism_confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = LocationForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('DanishTourism_Locations.html')
        else:
            return redirect('DanishTourism_EditLocation.html')


def Edit(request):
    form = LocationForm(request.POST or None)
    locations = Location.Locations.all()
    if form.is_valid():
        form.save()
        return redirect('DanishTourism_Locations')
    else:
        print(form.errors)
        form = LocationForm
    context = {
        'form': form,
        'locations': locations
    }
    return render(request, 'DanishTourism_EditLocation.html', context)


def get_tours(request):
    req = requests.get('https://www.bookmundi.com/denmark/tour-operators')  # Make request
    web_s = req.text  # Get the content of the request
    soup = BeautifulSoup(web_s, "html.parser")  # Parse
    # Targeting h4 elements
    top_tours = {
        'tour1': soup.find_all('h4')[0].get_text(),
        'tour2': soup.find_all('h4')[1].get_text(),
        'tour3': soup.find_all('h4')[2].get_text(),
        'tour4': soup.find_all('h4')[3].get_text(),
        'tour5': soup.find_all('h4')[4].get_text(),
    }
    return render(request, "DanishTourism_tourWidget.html", top_tours)


def flights_api(request):
    form = FlightsForm(data=request.GET or None)
    if request.method == 'GET':
        if form.is_valid():  # Checks to see if the submitted form is valid
            form.save()  # Saves the new location
            origin = request.GET.get('origin')
            destination = request.GET.get('destination')
            date = request.GET.get('date')
            returnDate = request.GET.get('returnDate')
            url = "https://skyscanner50.p.rapidapi.com/api/v1/searchFlights"
            querystring = {
                "origin": origin,
                "destination": destination,
                "date": date,
                "returnDate": returnDate,
                "currency": "USD",
            }
            headers = {
                "content-type": "application/octet-stream",
                "X-RapidAPI-Key": "a2a0ce4470msheb757e389450a32p1f90d0jsn3353435075a1",
                "X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            result1 = {"airline": response.json()['data'][0]['carriers']['name'],
                       "departure": response.json()['data'][0]['destination']['departure'],
                       "arrival": response.json()['data'][0]['destination']['arrival'],
                       "price": response.json()['data'][0]['price']['amount']
                       },
            result2 = {"airline": response.json()['data'][1]['carriers']['name'],
                       "departure": response.json()['data'][1]['destination']['departure'],
                       "arrival": response.json()['data'][1]['destination']['arrival'],
                       "price": response.json()['data'][1]['price']['amount']
                       },
            result3 = {"airline": response.json()['data'][2]['carriers']['name'],
                       "departure": response.json()['data'][2]['destination']['departure'],
                       "arrival": response.json()['data'][2]['destination']['arrival'],
                       "price": response.json()['data'][2]['price']['amount']
                       },
            result4 = {"airline": response.json()['data'][3]['carriers']['name'],
                       "departure": response.json()['data'][3]['destination']['departure'],
                       "arrival": response.json()['data'][3]['destination']['arrival'],
                       "price": response.json()['data'][3]['price']['amount']
                       },
            result5 = {"airline": response.json()['data'][4]['carriers']['name'],
                       "departure": response.json()['data'][4]['destination']['departure'],
                       "arrival": response.json()['data'][4]['destination']['arrival'],
                       "price": response.json()['data'][4]['price']['amount']
                       },
            content = {
                'result1': result1,
                'result2': result2,
                'result3': result3,
                'result4': result4,
                'result5': result5,
            }
            return render(request, 'DanishTourism_FlightResults.html', content)


def plan_trip(request):
    # Retrieves the Flights form
    form = FlightsForm(data=request.GET or None)
    # Checks if request method is GET
    if request.method == 'GET':
        if form.is_valid():  # Checks to see if the submitted form is valid
            return redirect('DanishTourism_FlightResults')  # Forwards to Flight Results Page
    content = {'form': form}  # Saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'DanishTourism_PlanTrip.html', content)
