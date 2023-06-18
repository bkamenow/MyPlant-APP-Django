from django.shortcuts import render

# Create your views here.


def create_profile(request):
    return render(request, template_name='accounts/create-profile.html')


def edit_profile(request):
    return render(request, template_name='accounts/edit-profile.html')


def profile_details(request):
    return render(request, template_name='accounts/profile-details.html')


def delete_profile(request):
    return render(request, template_name='accounts/delete-profile.html')




