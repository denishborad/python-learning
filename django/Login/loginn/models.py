from django.db import models

# Create your models here.

class UserRegister(models.Model):
    username = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    Email = models.EmailField()
    password1 = models.CharField(max_length=15)

class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=15)
