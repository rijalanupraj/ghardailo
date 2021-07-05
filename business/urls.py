# External Import
from django.urls import path
from .import views

# Internal Import


urlpatterns = [
    path('business-profile/', views.BusinessProfile, name='business-profile')
   
]
