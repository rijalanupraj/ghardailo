# External Import
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('accounts.urls')),
    path('', include('homepage.urls')),
    # path('', include('Customer.urls')),
    path('a/', include('admindashboard.urls'))
]

# Static & Media Management Files For Debug Mode Only.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
