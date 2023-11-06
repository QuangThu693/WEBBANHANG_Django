from django.urls import path
from .views import HomeView, LoginView, RegisterView, AllProductView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('all-product/', AllProductView.as_view(), name='all_product'),
]

