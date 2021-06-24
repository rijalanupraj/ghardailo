# External Import
from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('customer.urls')),
    path('mybusiness/', include('business.urls')),
]
