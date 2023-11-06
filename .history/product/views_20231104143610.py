from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import View
from .models import Category, Product, MenuItem

# Create your views here.
# def menu(request):
#   # menu_items = MenuItem.objects.all()
#   context = {'menu': menu}
#   return render(request, 'homepage/index.html', context)

def menu(request):
  menu = MenuItem.objects.all().values()
  # menu = {'Shoes', 'Shirt', 'Dress'}
  template = loader.get_template('homepage/header.html')
  context = {'menu': menu, }
  return HttpResponse(template.render(context, request))