from django.shortcuts import render
from django import forms
from django.views import View
from .models import CustomerUser

from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.



