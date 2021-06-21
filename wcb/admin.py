from django.contrib import admin
from .models import *

class WCBAdmin(admin.ModelAdmin):
    list_display = ('hiring',)
admin.site.register(WCB, WCBAdmin)
