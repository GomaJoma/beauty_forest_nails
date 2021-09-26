from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', None)


def rules(request):
    return render(request, 'main/rules.html', None)


def about_us(request):
    return render(request, 'main/about_us.html', None)


def contacts(request):
    return render(request, 'main/contacts.html', None)
