from django.urls import path
from . import views

urlpatterns = [
   path ('',views.Model_1,name='model1'),
   path ('model2/',views.Model_2,name='model2'),
   path ('model3/',views.Model_3,name='model3'),
   path ('home/',views.Home,name='home'),
   path ('contactus/',views.Contact_us,name='contactus'),
   path ('index/', views.index_view,name='index'),
]
