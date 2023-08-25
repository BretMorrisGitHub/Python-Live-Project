from django.urls import path
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.itemsApp_home, name="itemsApp_home"),
    path('new_item/', views.new_item, name="new_item"),
    path('details/', views.select_item, name="select_item"),
    path('<int:pk>/details/', views.item_details, name="item_details"),
    path('<int:pk>/edit_form/', views.edit_form, name="edit_items"),
    path('edit_item/', views.edit_page, name="edit_page"),
    path('details/<int:pk>/delete/', views.delete_item, name="delete_item"),
    path('api/', views.api, name="api"),
    path('scrape/', views.books_scraped, name="book_scrape"),
]

