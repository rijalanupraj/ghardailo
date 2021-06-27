from django.urls import path, include
from . import views 

urlpatterns = [
    path('dashboard', views.dashboard),
    path('service', views.service),
    path('business', views.business),
    path('customer', views.customer),
    path('activities', views.activities),
]