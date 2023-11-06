from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register , name='register'),
     path('login/', views.login_view, name='login'),
     path('success/', views.success_view, name='success_url'),
     path('logout/', LogoutView.as_view(), name='logout', kwargs={'next_page': 'home'}),
]