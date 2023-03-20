from django.contrib.sessions.models import Session
from django.contrib import admin
from beautifile.models import Register, Login, contactus, Product, UserDetails, Session, LinkGenerate
# Register your models here.
admin.site.register(Login)
admin.site.register(Register)
admin.site.register(Product)
admin.site.register(Session)
admin.site.register(UserDetails)
admin.site.register(LinkGenerate)


class contactusAdmin(admin.ModelAdmin):
    list_display = ("Yourname", "Subject", "Yourmail", "Message")


admin.site.register(contactus, contactusAdmin)
