from django.shortcuts import render
from django.views import View
from .models import Category, Product

# Create your views here.
# def menuView(request, category_id):
#   menu = Category.objects.get(pk = category_id)
#   render(request, 'homepage/detailProducts.html', {'category': menu})