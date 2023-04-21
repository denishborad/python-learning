import pprint
from django.contrib import admin
from .models import contactus, Users, LinkGenerate
from django.contrib.sessions.models import Session

# Register your models here.

admin.site.register(contactus)
admin.site.register(Users)
admin.site.register(LinkGenerate)

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n','<br>\n')
    _session_data.allow_tags = True
    list_display = ['session_key', '_session_data']
    readonly_fields = ['_session_data']
    exclude = ['session_data']

admin.site.register(Session, SessionAdmin)