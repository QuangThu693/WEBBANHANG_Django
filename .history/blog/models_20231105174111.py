from django.db import models

# Create your models here.
class Slider(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to='sliders/')
  description = models.TextField()
  link = models.URLField()
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title