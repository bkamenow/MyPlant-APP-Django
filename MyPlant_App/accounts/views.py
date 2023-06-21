from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from MyPlant_App.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from MyPlant_App.accounts.models import UserModel
from MyPlant_App.plants.models import PlantModel


# Create your views here.

def get_profile():
    try:
        return UserModel.objects.get()
    except UserModel.DoesNotExist as ex:
        return None


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, template_name='accounts/create-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template_name='accounts/edit-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    plants = PlantModel.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, template_name='accounts/profile-details.html', context=context)


def delete_profile(request):
    profile = get_profile()
    plants = PlantModel.objects.all()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        for plant in plants:
            plant_form = DeleteProfileForm(request.POST, instance=plant)
            plant_form.save()

        return redirect('home_page')

    context = {
        'profile': profile
    }
    return render(request, template_name='accounts/delete-profile.html')



