from django.urls import path

from MyPlant_App.accounts.views import create_profile, edit_profile, profile_details, delete_profile

urlpatterns = [
    path('create/', create_profile, name='create_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('details/', profile_details, name='profile_details'),
    path('delete/', delete_profile, name='delete_profile'),
]
