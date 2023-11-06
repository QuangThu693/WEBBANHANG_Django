from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.CharField(default='', max_length=100)
  parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children' )
  def __str__(self):
    return self.title

class Product(models.Model):
  name = models.CharField(max_length=255, verbose_name='Tên sản phẩm', default='')
  image_url = models.URLField(verbose_name='Link hình ảnh', default='https://example.com/default-image.jpg')
  description  = models.TextField(default='')
  category = models.ForeignKey(Category, on_delete= models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Giá')
  discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Giá khuyến mãi')

  def __str__(self):
    return self.name

class Variation(models.Model):
  product  = models.ForeignKey(Product, on_delete=models.CASCADE)
  title = models.CharField(max_length=255, default='')
  price = models.IntegerField(default=0)
  sale_price = models.IntegerField(default=0)
  active = models.BooleanField(default=True)
  def __str__(self):
    return self.title

class MenuItem(models.Model):
  title = models.CharField(max_length=100)
  def __str__(self):
    return self.title