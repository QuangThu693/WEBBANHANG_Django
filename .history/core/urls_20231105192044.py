from django.urls import path
from .views import HomeView, AllProductView
from product.views import HomeView
from blog.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('all-product/', AllProductView.as_view(), name='all_product'),
]

