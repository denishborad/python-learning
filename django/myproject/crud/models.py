from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.shortcuts import redirect
from PIL import Image

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True)
    firstname = models.CharField(max_length=50,null=True, blank=True)
    lastname = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    pass1 = models.CharField(max_length=12)
    pass2 = models.CharField(max_length=12)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField()
    mobile_no = models.IntegerField(blank=True, null=True)
    prof_img = models.ImageField(
        upload_to='images/', blank=True, null=True, default="images.png")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)
    
    # @classmethod
    # def create(cls, username, firstname, lastname, email, pass1, pass2):
    #     u = Users(username=username, firstname=firstname, lastname=lastname, email=email, pass1=pass1,pass2=pass1)
    #     if pass1 != pass2:
    #         messages.error('please!! Your Both Password Are Same??')
    #         return u
    #     u.save()
    #     return u

    @classmethod
    def update_profile(cls,userid, username, firstname, lastname, email, dob, address, mobile_no, prof_img):
        pro = cls.objects.filter(userid = userid)
        pro = pro.first()
       
        pro.username = username
        pro.firstname = firstname
        pro.lastname = lastname
        pro.email = email
        pro.dob = dob
       
        pro.address = address
        pro.mobile_no = mobile_no
        pro.prof_img = prof_img
        pro.save()
        return pro
    
    @classmethod
    def update_pass(cls,userid,pass1):
        pro = cls.objects.filter(userid = userid)
        print(pro,'pro')
        pro.pass1 = pass1
        pro.save()
        return pro
    
    # @classmethod
    # def set_password(self, pass1):
        
    #     self._pass1 = pass1
 
    def check_password(self, pass1):
        def Setter(pass1):
            print(pass1,'pass1')
            self.set_password(pass1)
            # Password hash upgrades shouldn't be considered password changes.
            self._pass1 = pass1
            self.save(update_fields=["pass1"])
        return check_password(pass1, self.pass1, Setter)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.prof_img.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.prof_img.path)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users,  on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    token = models.CharField(max_length=500, null=True)
    session_status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    is_deleted = models.BooleanField(default=0,null=True)
    def __str__(self):
        return self.session_id
    

class contactus(models.Model):
    Subject = models.CharField(max_length=200)
    Yourname = models.CharField(max_length=100)
    Yourmail = models.EmailField()
    Message = models.TextField()

class LinkGenerate(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=300, unique=True)
    expiry = models.CharField(default="s", max_length=500)
    status = models.BooleanField()

    def __str__(self):
        return self.email