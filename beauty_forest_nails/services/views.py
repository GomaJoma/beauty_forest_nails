from django.shortcuts import render
from .models import Service


def services(request):
    services_list = Service.objects.all()
    context = {
        'services_list': services_list
    }
    return render(request, 'services/services.html', context)
