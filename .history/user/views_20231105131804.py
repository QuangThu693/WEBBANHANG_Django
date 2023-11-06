from django.shortcuts import render
from django import forms
from django.views import View
from .models import CustomerUser

from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success_url')  # Thay 'success_url' bằng URL chuyển hướng sau khi đăng ký thành công
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


