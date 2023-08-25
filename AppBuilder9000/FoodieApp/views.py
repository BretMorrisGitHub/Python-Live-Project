from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeForm
import requests
import json

# Creating basic app
def foodie_home(request):
    return render(request, 'FoodieApp/foodie_home.html')

# Displays list of added recipes
def foodie_recipes(request):
    recipe = Recipe.objects.all()
    content = {'recipe':recipe}
    return render(request, 'FoodieApp/foodie_recipes.html', content)

# Allows users to create a recipe to share on app
def foodie_create_recipe(request):
        form = RecipeForm(data=request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('foodie_recipes')
        content = {'form' : form}
        return render(request, 'FoodieApp/foodie_create_recipe.html', content)

# Displays the about page
def foodie_about(request):
    return render(request, 'FoodieApp/foodie_about.html')

# Displays recipe details
def foodie_details(request, pk):
    pk = int(pk)
    recipe = get_object_or_404(Recipe, pk=pk)
    content = {'recipe': recipe}
    return render(request, 'FoodieApp/foodie_details.html', content)

# Allows users to edit recipes
def foodie_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data= request.POST or None, instance=recipe)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('foodie_recipes')
    content = {'form': form, 'recipe': recipe}
    return render(request, 'FoodieApp/foodie_edit.html', content)

# Allow user to delete recipe
def foodie_delete(request, pk):
    pk = int(pk)
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=recipe)
    if request.method == 'POST':
        if form.is_valid():
            recipe.delete()
            return redirect('foodie_recipes')
    content = {'form': form, 'recipe': recipe}
    return render(request, 'FoodieApp/foodie_delete.html', content)

# API request to display random drink
def foodie_api(request):
    response = requests.get('http://www.thecocktaildb.com/api/json/v1/1/random.php')
    random_drink = json.loads(response.text)

    for i in random_drink['drinks']:
        name = i['strDrink']
        instructions = i['strInstructions']
        ingredient1 = i['strIngredient1']
        ingredient2 = i['strIngredient2']
        ingredient3 = i['strIngredient3']
        ingredient4 = i['strIngredient4']


    content = {"name": name, "instructions": instructions, "ingredient1": ingredient1, "ingredient2": ingredient2,
               "ingredient3": ingredient3, "ingredient4": ingredient4}
    return render(request, 'FoodieApp/foodie_api.html', content)