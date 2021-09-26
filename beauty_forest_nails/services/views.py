from django.shortcuts import render, get_list_or_404
from .models import Service


def services(request):
    services_list = get_list_or_404(Service)
    context = {
        'services_list': services_list
    }
    return render(request, 'services/services.html', context)
