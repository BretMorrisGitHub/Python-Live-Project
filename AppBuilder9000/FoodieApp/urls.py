from django.urls import path
from . import views

urlpatterns = [
    path('', views.foodie_home, name='foodie_home'),
    path('recipes/', views.foodie_recipes, name='foodie_recipes'),
    path('create_recipe/', views.foodie_create_recipe, name='foodie_create_recipe'),
    path('about/', views.foodie_about, name='foodie_about'),
    path('<int:pk>/details/', views.foodie_details, name='foodie_details'),
    path('<int:pk>/edit/', views.foodie_edit, name='foodie_edit'),
    path('<int:pk>/delete/', views.foodie_delete, name='foodie_delete'),
    path('api/', views.foodie_api, name='foodie_api'),
]