from django.contrib import admin
from .models import *

class WorkerAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'picture', 'phone', 'is_active')
admin.site.register(Worker, WorkerAdmin)