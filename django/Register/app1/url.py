from django.urls import path
from . import views

urlpatterns = [
    path('', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('home/', views.Home, name='home')
]
