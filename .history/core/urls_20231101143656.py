from django.urls import path
from .views import HomeView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', LoginView.as_view(), name='register'),
]
