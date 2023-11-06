from django.shortcuts import render
from django import forms
from django.views import View
from .models import CustomerUser

from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.
User = get_user_model()

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'homepage/register.html'
    success_url = reverse_lazy('login')



