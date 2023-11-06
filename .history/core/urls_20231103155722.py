from django.urls import path
from .views import HomeView, LoginView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
     path('menu/', views.menu, name='menu'),
]
