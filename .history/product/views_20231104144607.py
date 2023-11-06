from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import View
from .models import Category, Product, MenuItem

# Create your views here.
def menu(request):
  menu_items = MenuItem.objects.all()
  menu = {'Shoes', 'Shirt', 'Dress'}
  context = {'menu': menu}
  return render(request, 'homepage/index.html', context)
