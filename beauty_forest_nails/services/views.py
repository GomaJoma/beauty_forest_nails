from django.shortcuts import render, get_list_or_404
from .models import Service


def services(request, service_type='all'):
    if service_type == 'all':
        services_list = get_list_or_404(Service)
    else:
        services_list = Service.objects.filter(type=service_type)
    context = {
        'services_list': services_list,
        'service_type': service_type,
    }
    return render(request, 'services/services.html', context)
