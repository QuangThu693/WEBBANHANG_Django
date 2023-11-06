from django.shortcuts import render
from django.views import View
from .models import Slider

# Create your views here.
class HomeView(View):
  def slider_list(request):
    sliders = Slider.objects.filter(is_active=True)
    return render(request, 'homepage/index.html', {'sliders': sliders})