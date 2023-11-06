from django.db import models
from user.models import CustomerUser

# Create your models here.
class Order(models.Model):
  user = models.ForeignKey(CustomerUser, on_delete= models.CASCADE)
