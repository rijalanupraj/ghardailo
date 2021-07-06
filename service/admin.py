
from django.contrib import admin

# importing from model
from .models import Services

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('icon_text', 'name', 'is_active', 'description')

admin.site.register(Services, ServicesAdmin)