from django.contrib import admin  
from .models import UserRegister,UserLogin
# Register your models here.
admin.site.register(UserRegister)
admin.site.register(UserLogin)
