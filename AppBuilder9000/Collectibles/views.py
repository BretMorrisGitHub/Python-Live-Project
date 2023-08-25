from django.shortcuts import render, redirect, get_object_or_404
from .forms import CardsForm
from .models import Cards
from bs4 import BeautifulSoup
import requests
import json

# Story #1: Build the basic app---------------------------------
def collectibles_create(request):
    if request.method == 'POST':
        form = CardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('collectibles_home') # Redirects to the desired page after saving
    else:
        form = CardsForm()

    return render(request, 'Collectibles/create.html', {'form': form})

def collectibles_home(request):
    return render(request, 'Collectibles/collectibles_home.html')

def collectibles_display(request):
    cards = Cards.objects.all()
    content = {'cards': cards}
    return render(request, 'Collectibles/collectibles_display.html', content)

def collectibles_details(request, item_id):
    item = get_object_or_404(Cards, pk=item_id)
    context = {'item': item}
    return render(request, 'Collectibles/collectibles_details.html', context)



def collectibles_update(request, item_id):
    item = get_object_or_404(Cards, pk=item_id)
    form = CardsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('Collectibles/collectibles_details.html')
    content = {'form': form, 'item': item}
    return render(request, 'Collectibles/collectibles_update.html', content)

def collectibles_delete(request, item_id):
    item = get_object_or_404(Cards, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('../../display')
    content = {'item': item}
    return render(request, 'Collectibles/collectibles_delete.html', content)

# Story #6 BS pt 1----Set up BS and parse img from card-price website.
def collectibles_bsoup(request):
    page = requests.get("https://www.pricecharting.com/game/pokemon-japanese-vstar-universe/pikachu-205")
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.find_all("img")
    # print(soup.prettify())
    test = images[3]['src']
    content = {'images': images, 'test': test}
    return render(request, 'Collectibles/collectibles_bsoup.html', content)

def collectibles_api(request):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard/")
    pokemon_data = response.json()

    content = {
        'name': pokemon_data['name'],
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        }

    return render(request, 'Collectibles/collectibles_api.html', content)


