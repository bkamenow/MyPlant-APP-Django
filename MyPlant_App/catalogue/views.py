from django.shortcuts import render

from MyPlant_App.accounts.views import get_profile
from MyPlant_App.plants.models import PlantModel


# Create your views here.


def show_catalogue(request):
    profile = get_profile()
    plants = sorted(PlantModel.objects.all(), key=lambda x: x.pk)

    context = {
        'plants': plants,
        'plants_len': len(plants),
        'profile': profile
    }
    return render(request, template_name='common/catalogue.html', context=context)
