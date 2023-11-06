from django.shortcuts import render
from .models import Slider

# Create your views here.
def slider_list(request):
  sliders = Slider.objects.filter(is_active=True)
  return render(request, 'slider/slider_list.html', {'sliders': sliders})