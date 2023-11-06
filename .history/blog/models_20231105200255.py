from django.db import models

# Create your models here.
class Slider(models.Model):
  title = models.CharField(max_length=100)
  image = models.URLField(default='')
  description = models.TextField()
  link = models.URLField(default='')
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title

class Banner(models.Model):
  title = models.CharField(max_length=100)
  image = models.URLField(default='')
  link = models.URLField(default='')
  description = models.TextField(blank=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title