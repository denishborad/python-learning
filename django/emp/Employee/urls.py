from django.urls import path
from . import views

urlpatterns = [
    path('',views.create,name='create'),
    path('list/',views.list1,name='list'),
    path('edit/<int:emp_id>',views.edit,name='edit'),
    path('edit/updaterecord/<int:emp_id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:emp_id>',views.delete,name='delete'),
]