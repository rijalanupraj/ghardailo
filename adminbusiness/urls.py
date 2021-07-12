from django.urls import path, include
from . import views 

urlpatterns = [
    path('dashboard', views.businessDashboard, name="businessDash"),
    path('edit-profile', views.editProfile, name="editProfileBus"),

    # for service
    path('getService',views.getService, name="getServiceDash"),
    path('postService',views.postService, name="postServiceDash"),
    path('updateService/<int:service_id>', views.updateService, name="updateServiceDash"),
    path('deleteService/<int:service_id>', views.deleteService, name="postServiceDash"),


 
]