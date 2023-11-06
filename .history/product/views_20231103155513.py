from django.shortcuts import render
from django.views import View
from .models import Category, Product

# Create your views here.

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'header.html', {'menu_items': menu_items})