from django.urls import path

from MyPlant_App.catalogue.views import show_catalogue

urlpatterns = [
    path('catalogue/', show_catalogue, name='show_catalogue')
]
