from django.urls import path, include
from . import views 

urlpatterns = [
    path('dashboard', views.businessDashboard, name="businessDash"),

    # for service
    path('getService',views.getService, name="getServiceDash"),
    path('postService',views.postService, name="postServiceDash"),
    path('updateService/<int:service_id>', views.updateService, name="updateServiceDash"),
    path('deleteService/<int:service_id>', views.deleteService, name="deleteServiceDash"),

    # for Worker
    path('getWorker',views.getWorker, name="getWorkerDash"),
    path('postWorker',views.postWorker, name="postWorkerDash"),
    path('updateWorker/<int:Worker_id>', views.updateWorker, name="updateWorkerDash"),
    path('deleteWorker/<int:Worker_id>', views.views.deleteWorker, name="deleteWorkerDash"),

    #for profile
    path('getProfile',views.getProfile, name="getProfileDash"),
    path('editBusiness',views.editBusiness, name="editBusinessDash"),
    path('editBusinessProfile',views.editBusinessProfile, name="editBusinessProfileDash"),
    path('updateProfile/<int:profile_id>', views.updateProfile, name="updateProfileDash"),

    path('changePassword', views.change_password, name='changePasswordDash'),
 
]