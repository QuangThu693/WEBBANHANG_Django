from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django import forms
from django.views import View
from .models import CustomerUser

# Create your views here.

# Register
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

# Register success
def success_view(request):
  user = request.user
  return render(request, 'homepage/user/register_success.html', {'user': user})

# Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Chuyển hướng sau khi đăng nhập thành công
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


