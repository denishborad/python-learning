from django.db import models

# # Create your models here.
class Sign_up(models.Model):
    yourname = models.CharField(max_length=150)
    email = models.EmailField()
    password1 = models.CharField(max_length=12)
    password2 = models.CharField(max_length=12)

class Login(models.Model):
    yourname = models.CharField(max_length=150)
    password1 = models.CharField(max_length=12)
