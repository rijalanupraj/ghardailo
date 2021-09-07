from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.businessDashboard, name="businessDash"),

    # for service
    path('getService', views.getService, name="getServiceDash"),
    path('postService', views.postService, name="postServiceDash"),
    path('updateService/<int:service_id>',
         views.updateService, name="updateServiceDash"),
    path('deleteService/<int:service_id>',
         views.deleteService, name="deleteServiceDash"),

    # for Worker
    path('getWorker', views.getWorker, name="getWorkerDash"),
    path('postWorker', views.Worker_registration, name="postWorkerDash"),
    path('updateWorker/<int:Worker_id>',
         views.updateWorker, name="updateWorkerDash"),
    path('deleteWorker/<int:Worker_id>',
         views.deleteWorker, name="deleteWorkerDash"),

    # for profile
    path('getProfile', views.getProfile, name="getProfileDash"),
    path('editBusiness', views.editBusiness, name="editBusinessDash"),
    path('editBusinessProfile', views.editBusinessProfile,
         name="editBusinessProfileDash"),
    path('updateProfile/<int:profile_id>',
         views.updateProfile, name="updateProfileDash"),

    path('changePassword', views.change_password, name='changePasswordDash'),

    # For Hiring
    path('hirings/', views.BusinessHiringListView.as_view(),
         name='business-hiring-list'),
    path('hirings/approve/<int:id>', views.approve_business_hiring,
         name='approve_business_hiring'),
     path('hirings/complete/<int:id>', views.complete_business_hiring,
         name='complete_business_hiring'),
    path('hirings/reject/<int:id>', views.reject_business_hiring,
         name='reject_business_hiring'),

     #for notification
     path('api/notification/<int:notification_pk>',
         views.HireNotificationView.as_view(), name='business-hire-notification-api'),
     path('notifications/', views.AllNotificationPageView.as_view(),
         name="business-all-notification-page"),

]
