from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# from django.contrib.auth import get_user_model
# Create your models here.


class contactus(models.Model):
    Subject = models.CharField(max_length=200)
    Yourname = models.CharField(max_length=100)
    Yourmail = models.EmailField()
    Message = models.TextField()


class Products:
    id: int
    bursh_text: str
    lorem_text: str
    image_1: str
    price_text: int


class Product(models.Model):
    pTitle = models.CharField(max_length=50)
    pDesc = models.CharField(max_length=200)
    pImages = models.ImageField()
    pPrice = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pTitle


class Login(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.user


class Register(models.Model):
    uname = models.CharField(max_length=100)
    profile_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    repassword = models.CharField(max_length=12)

    def __str__(self):
        return self.uname


# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     uname = models.CharField(max_length=150, null=True)
#     email = models.EmailField(null=True)
#     profile_pic = models.ImageField(upload_to='images/', blank=True, null=True)
#     dob = models.DateField(blank=True, null=True)
#     mobile_no = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return str(self.user)


class UserDetails(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(
        upload_to='images/', blank=True, null=True, default="images.png")
    dob = models.DateField(blank=True, null=True)
    email = models.EmailField(null=True)
    mobile_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey("user",  on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    token = models.CharField(max_length=50, null=True)
    session_status = models.BooleanField(null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(null=True)


class LinkGenerate(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=300, unique=True)
    expiry = models.CharField(default="s", max_length=500)
    status = models.BooleanField()
