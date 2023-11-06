from django.urls import path
from . import views

urlpatterns = [
    path('register01/', views.register , name='register01'),
]