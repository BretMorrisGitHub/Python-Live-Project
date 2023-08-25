from django.urls import path
from . import views

urlpatterns = [
    path('', views.prophound_home, name='prophound_home'),
    path('create/', views.prophound_create, name='prophound_create'),
    path('read/', views.prophound_read, name='prophound_read'),
    path('<int:pk>/details/', views.prophound_details, name='prophound_details'),
    path('<int:pk>/edit/', views.prophound_edit, name='prophound_edit'),
    path('<int:pk>/delete/', views.prophound_delete, name='prophound_delete'),
    path('api/', views.prophound_api, name='prophound_api'),
]