from django.shortcuts import render

# Create your views here.


def show_catalogue(request):
    return render(request, template_name='common/catalogue.html')
