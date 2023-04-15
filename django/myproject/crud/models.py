from django.db import models
from PIL import Image

# Create your models here.
class SignUp(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True)
    firstname = models.CharField(max_length=50,null=True, default=False, blank=True)
    lastname = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    pass1 = models.CharField(max_length=12)
    pass2 = models.CharField(max_length=12)
    prof_img = models.ImageField(
        upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    userprof = models.OneToOneField(
        SignUp, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=50,null=True)
    firstname = models.CharField(max_length=50,null=True)
    lastname = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    dob = models.DateField(blank=True, null=True)
    address = models.TextField()
    mobile_no = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='images/', blank=True, null=True, default="images.png")
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class contactus(models.Model):
    Subject = models.CharField(max_length=200)
    Yourname = models.CharField(max_length=100)
    Yourmail = models.EmailField()
    Message = models.TextField()
