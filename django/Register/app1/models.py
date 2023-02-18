from django.db import models

# Create your models here.
class sign_up(models.Model):
    user_name = models.CharField(max_length=50)
    Email = models.EmailField()
    pass1 = models.CharField(max_length=12)

class log_in(models.Model):
        user_name = models.CharField(max_length=50)
        pass1 = models.CharField(max_length=12)
