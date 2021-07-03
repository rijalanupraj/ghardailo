# External Import
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('', include('accounts.urls')),
    path('mybusiness/', include('business.urls')),
    path('', include('homepage.urls'))
]

# Static & Media Management Files For Debug Mode Only.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
