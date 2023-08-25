import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


# Create your views here.
def itemsApp_home(request):
    """Function to open the homepage."""
    return render(request, 'ItemsApp/home.html')


def new_item(request):
    """Creates the form used for user input"""
    form = ItemForm(data=request.POST or None)  # Creates the form from forms.py.
    # Make only the name and image required.
    for field in form.fields:
        form.fields[field].required = False
        form.fields['name'].required = True
        form.fields['image'].required = True

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('select_item')
    content = {'form': form}  # Dictionary for form data entry.
    return render(request, 'ItemsApp/new_item.html', content)

def select_item(request):
    """Creates a list of items from the database with anchor tag to select."""
    item_list = Item.objects.all()  # Grabs all items from all items in the database.
    content = {'item_list': item_list}
    return render(request, "ItemsApp/details.html", content)


def item_details(request, pk):
    """Displays the chosen item from 'select_item' function."""
    pk = int(pk)
    item_get = Item.objects.filter(pk=pk)
    content = {'item_get': item_get}
    return render(request, "ItemsApp/details_page.html", content)


def edit_page(request):
    """Page that displays a drop-down menu for editing items in the database."""
    items = Item.objects.all()
    return render(request, 'ItemsApp/edit_page.html', {'items': items})


def edit_form(request, pk):
    """Renders a new page for input and edit form."""
    pk = int(pk)
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('select_item')
        else:
            print(form.errors)
    else:
        return render(request, 'ItemsApp/edit_items.html', {'form': form})


def delete_item(request, pk):
    """Grabs the information from the primary key of the item to delete."""
    pk = int(pk)
    item = get_object_or_404(Item, pk=pk)
    # If the item is not null, delete the item.
    if item is not None:
        item.delete()
        return redirect('select_item')
    else:
        return redirect('select_item')

def api(request):
    url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'

    headers = {
        'User-Agent': '@UnknwnEntity#2059'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # raise exception if response status code is not 200
        api_data = response.json()
        
        content = {'success': True, 'data': api_data}

    except requests.exceptions.HTTPError as e:
        # handle exceptions caused by non-200 status codes
        content = {'success': False, 'message': f'An error occurred: {e}'}

    return render(request, 'ItemsApp/api.html', content)

def books_scraped(request):
    # Webpage request to grab the skeleton of the web page.
    page = requests.get('http://books.toscrape.com/')

    # Grabs the page source and stores it into the variable 'soup'.
    soup = BeautifulSoup(page.content, 'html.parser')

    # Book list inside of the section tag.
    books = soup.find('section')

    """Titles"""
    book_titles = books.select(".product_pod h3")
    titles = [t.get_text() for t in book_titles]

    content = {'titles': titles}

    return render(request, 'ItemsApp/scrape.html', content)

