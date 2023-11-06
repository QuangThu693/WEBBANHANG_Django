from django.shortcuts import render
from django.views import View
from product.models import MenuItem, Category

# Create your views here.
class HomeView(View):
  def get(self, request):
    menuList = MenuItem.objects.all()
    category = Category.objects.all()
    context = {'menu': menuList,}
    return render(request, 'homepage/index.html', context)

class LoginView(View):
  def get(self, request):
    return render(request, 'homepage/user/login.html')

class RegisterView(View):
  def get(self, request):
    return render(request, 'homepage/user/register.html')

