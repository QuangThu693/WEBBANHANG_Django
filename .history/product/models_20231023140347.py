from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.CharField(default='', max_length='')
  slug = models.CharField(max_length=100, default='')
  description = models.TextField(default='')
  active = models.BooleanField(default= True)

class Product(models.Model):
  tittle = models.CharField(max_length=255, default='')
  description  = models.TextField(default='')
  category = models.ForeignKey(Category, on_delete= models.CASCADE)
  price = models.IntegerField(default= 0)
  active = models.BooleanField(default=True)