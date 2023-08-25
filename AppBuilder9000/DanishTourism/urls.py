from django.urls import path
from . import views

urlpatterns = [
    #   Sets the url path to home page index.html
    path('', views.DanishTourism_home, name='DanishTourism_home'),
    path('DanishTourism_AddLocation/', views.add_location, name='DanishTourism_AddLocation'),
    path('DanishTourism_Locations', views.displayLocations, name='DanishTourism_Locations'),
    path('<int:pk>/details/', views.displayDetails, name='DanishTourism_ViewDetails'),
    path('DanishTourism_EditLocation', views.Edit, name='DanishTourism_EditLocation'),
    path('<int:pk>/DanishTourism_confirmDelete', views.confirmed, name='DanishTourism_confirmed'),
    path('<int:pk>/delete/', views.delete, name='DanishTourism_delete'),
    path('<int:pk>/edit/', views.udDetails, name='DanishTourism_Edit'),
    path('DanishTourism_tourWidget', views.get_tours, name='DanishTourism_tourWidget'),
    path('DanishTourism_PlanTrip/', views.plan_trip, name='DanishTourism_PlanTrip'),
    path('DanishTourism_FlightResults', views.flights_api, name='DanishTourism_FlightResults')
]
