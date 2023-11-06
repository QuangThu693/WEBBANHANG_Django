from django.shortcuts import render
from django.views import View
from product.models import MenuItem

# Create your views here.
class HomeView(View):
  def get(self, request):
    return render(request, 'homepage/index.html')

class LoginView(View):
  def get(self, request):
    return render(request, 'homepage/user/login.html')

class RegisterView(View):
  def get(self, request):
    return render(request, 'homepage/user/register.html')

