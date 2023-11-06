from django.db import models
from product.models import Variation

# Create your models here.
class Cart(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  item = models.ForeignKey(Va)
