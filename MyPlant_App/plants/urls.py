from django.urls import path

from MyPlant_App.plants.views import create_plant, plant_details, edit_plant, delete_plant

urlpatterns = [
    path('create/', create_plant, name='create_plant'),
    path('details/<int:pk>/', plant_details, name='plant_details'),
    path('edit/<int:pk>/', edit_plant, name='edit_plant'),
    path('delete/<int:pk>/', delete_plant, name='delete_plant'),
]
