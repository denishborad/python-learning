from django.db import models

# Create your models here.
class Model1(models.Model):
    firstname = models.CharField(max_length=150)
    secondname =models.CharField(max_length=150)
    Email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    pass1 = models.CharField(max_length=12)

    def __str__(self):
        return self.firstname

class Model2(models.Model):
    firstname = models.CharField(max_length=150)
    pass1 = models.CharField(max_length=12)

    def __str__(self):
        return self.firstname

class Model3(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    yourname = models.CharField(max_length=100)
    youremail = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    yourmessage = models.TextField()

    def __str__(self):
        return self.yourname

class Index(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Roll_No = models.IntegerField(help_text="Enter ^ digit rol number")
    Password = models.CharField(max_length=15)

    def __str__(self):
        return self.First_Name
    
