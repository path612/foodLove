from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from . import models


# Create your views here.
class LunchForm(forms.Form):
    submitter = forms.CharField(label="Foodie's Name:)")
    food = forms.CharField(label="Your tasty food :p")


lunch_form = LunchForm(auto_id=False)


def index(request):
    lunches = models.Lunch.objects.all()
    return render(
        request,
        'main_app/food_form.html',
        {
            'lunches': lunches,
            'form': lunch_form
        }
    )


# @login_required
def home(request):
    return render(request, 'main_app/home.html')


def Login(request):
    form_class = AuthenticationForm
    form = form_class(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

    return render(request, 'main_app/food_form.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'main_app/signup.html', {'form': form})


def newlunch(request):
    l = models.Lunch()
    l.submitter = request.POST.get('submitter', False)
    l.food = request.POST.get('food', False)
    l.save()
    return redirect('home')
