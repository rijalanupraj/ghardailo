from django.contrib import admin
from .models import *

class HiringAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_time')
admin.site.register(Hiring, HiringAdmin)
