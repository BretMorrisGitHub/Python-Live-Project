from django.urls import path
from . import views

urlpatterns = [
    # sets the url path to home page index.html.
    path('', views.CookinGadget_home, name='CookinGadget_home'),
    # Sets the url path to Create New Account page CreateNewAccount.html.
]
