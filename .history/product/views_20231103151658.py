from django.shortcuts import render
from django.views import View
from .models import Category, Product

# Create your views here.

def menuListView(request):
  list_menu = Category.objects.all()
  context = {"list_category" : list_menu}
  return render(request, '../templates/homepage/header.html', context)

# def menuView(request, category_id):
#   menu = Category.objects.get(pk = category_id)
#   render(request, 'homepage/detailProducts.html', {'category': menu})