from django.shortcuts import render


def index(request):
    return render(request, 'index.html', None)


def rules(request):
    return render(request, 'rules.html', None)


def about(request):
    return render(request, 'about.html', None)


def contacts(request):
    return render(request, 'contacts.html', None)
