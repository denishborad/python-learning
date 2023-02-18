from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register, name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.Home,name='home'),
]