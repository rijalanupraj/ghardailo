from django.contrib import admin
from .models import *
# Register your models here.


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'logo', 'cover_picture', 'district',
                    'province', 'is_solo', 'street_address', 'description', 'phone')


admin.site.register(Business, BusinessAdmin)


class Business_ServiceAdmin(admin.ModelAdmin):
    list_display = ('business', 'service', 'description')


admin.site.register(Business_Service, Business_ServiceAdmin)
