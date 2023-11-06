from django.shortcuts import render
from django.views import View
from .models import Category, Product, MenuItem

# Create your views here.
def menu(request):
  menu_items = MenuItem.objects.all()
  return render(request, 'homepage/header.html', {'menu_items': menu_items})