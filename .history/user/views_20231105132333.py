from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django import forms
from django.views import View
from .models import CustomerUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success_url')
    else:
        form = RegistrationForm()
    return render(request, 'homepage/user/register.html', {'form': form})


