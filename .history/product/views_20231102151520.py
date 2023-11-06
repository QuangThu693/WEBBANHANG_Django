from django.shortcuts import render
from django.views import View
from .models import Category, Product

# Create your views here.
class MenuView(View):
  def get(self, category_id):
    menu = Category.objects.get(pk = category_id)