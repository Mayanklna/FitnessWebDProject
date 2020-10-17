from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm


def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('users:home')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('users:home')
    # else:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            messages.info(request, 'Username OR password is incorrect')

    else:
        return render(request, 'login.html')


def profilePage(request):
    return render(request, 'profile.html', {'username': request.user})


def logoutUser(request):
    logout(request)
    return redirect('users:login')


def home(request):
    return render(request, 'base.html')
