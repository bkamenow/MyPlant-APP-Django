from django.shortcuts import render

# Create your views here.


def create_plant(request):
    return render(request, template_name='plants/create-plant.html')


def plant_details(request):
    return render(request, template_name='plants/plant-details.html')


def edit_plant(request):
    return render(request, template_name='plants/edit-plant.html')


def delete_plant(request):
    return render(request, template_name='plants/delete-plant.html')

