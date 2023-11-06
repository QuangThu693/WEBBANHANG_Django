from django.shortcuts import render
from django.views import View
from .models import Category, Product, MenuItem

# Create your views here.
# class HomeView(View):
#   def get(self, request):
#     menuList = MenuItem.objects.all()
#     root_categories = Category.objects.filter(parent=None)
#     product = Product.objects.all()
#     context = {'menu': menuList,  'root_categories': root_categories, 'products': product,}
#     return render(request, 'homepage/index.html', context)
