from django.urls import path
from . import views


urlpatterns = [
    path('', views.collectibles_home, name='collectibles_home'),
    path('create/', views.collectibles_create, name='collectibles_create'),
    path('display/', views.collectibles_display, name='collectibles_display'),
    path('<int:item_id>/details/', views.collectibles_details, name='collectibles_details'),
    path('<int:item_id>/update/', views.collectibles_update, name='collectibles_update'),
    path('<int:item_id>/delete/', views.collectibles_delete, name='collectibles_delete'),
    path('bsoup/', views.collectibles_bsoup, name='collectibles_bsoup'),
    path('api/', views.collectibles_api, name='collectibles_api'),
]