from django.contrib import admin
from .models import Category, Product, Variation, MenuItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(MenuItem)
