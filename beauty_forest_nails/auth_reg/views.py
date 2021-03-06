from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, UserAuthenticationForm


# noinspection PyUnresolvedReferences
def auth_login(request):
    error = ''
    print(request.path)
    print(request.GET.get('next'))
    if request.method == 'POST':
        print(request.path)
        form = UserAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next'))
            else:
                error = 'Invalid login'
        else:
            error = 'Form not valid'
    else:
        form = UserAuthenticationForm()

    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'auth_reg/login.html', context)
    # pass


# noinspection PyUnresolvedReferences
def register(request):
    error = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Validation error'
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'auth_reg/register.html', context)


def logout_view(request):
    logout(request)
    return redirect(request.GET.get('next'))
