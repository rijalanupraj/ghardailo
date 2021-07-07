from django.urls import path, include
from . import views 

urlpatterns = [
    path('dashboard', views.businessDashboard, name="businessDash"),
    path('edit-profile', views.editProfile, name="editProfileBus"),
 
]