from django.contrib import admin

from .models import SignUp,contactus,UserProfile

# Register your models here.

admin.site.register(SignUp)
admin.site.register(contactus)
admin.site.register(UserProfile)