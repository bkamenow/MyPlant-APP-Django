from django.shortcuts import render

from MyPlant_App.accounts.views import get_profile


# Create your views here.


def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'base.html', context)
