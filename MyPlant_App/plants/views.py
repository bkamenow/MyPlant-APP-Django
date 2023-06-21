from django.shortcuts import render, redirect

from MyPlant_App.accounts.views import get_profile
from MyPlant_App.plants.forms import CreatePlantForm, EditPlantForm, DeletePlantForm
from MyPlant_App.plants.models import PlantModel


# Create your views here.
def get_plant(pk):
    plant = PlantModel.objects.filter(pk=pk).get()
    return plant


def create_plant(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_catalogue')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, template_name='plants/create-plant.html', context=context)


def plant_details(request, pk):
    plant = get_plant(pk)
    profile = get_profile()

    context = {
        'plant': plant,
        'profile': profile
    }

    return render(request, 'plants/plant-details.html', context)


def edit_plant(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    if request.method == 'GET':
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show_catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form
    }
    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show_catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form
    }
    return render(request, 'plants/delete-plant.html', context)
