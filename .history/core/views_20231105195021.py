from django.shortcuts import render
from django.views import View
from blog.models import Slider
from product.models import MenuItem, Category, Product

# Create your views here.
class HomeView(View):
  def get(self, request):
    sliders = Slider.objects.filter(is_active=True)
    menuList = MenuItem.objects.all()
    root_categories = Category.objects.filter(parent=None)
    product = Product.objects.all()
    context = {'menu': menuList,  'root_categories': root_categories, 'products': product,'sliders': sliders}
    return render(request, 'homepage/index.html', context)

class AllProductView(View):
  def get(self, request):
    return render(request, 'homepage/listProduct.html')



class LoginView(View):
  def get(self, request):
    return render(request, 'homepage/user/login.html')

class RegisterView(View):
  def get(self, request):
    return render(request, 'homepage/user/register.html')

