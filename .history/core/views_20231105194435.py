from django.shortcuts import render
from django.views import View
from blog.views import Slider

# Create your views here.
class HomeView(View):
  def get(self, request):
    sliders = Slider.objects.filter(is_active=True)
    return render(request, 'homepage/index.html')

class AllProductView(View):
  def get(self, request):
    return render(request, 'homepage/listProduct.html')



class LoginView(View):
  def get(self, request):
    return render(request, 'homepage/user/login.html')

class RegisterView(View):
  def get(self, request):
    return render(request, 'homepage/user/register.html')

