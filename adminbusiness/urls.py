from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.businessDashboard, name="business-dash"),

    # for service
    path('getService', views.getService, name="get-service-dash"),
    path('postService', views.postService, name="post-service-dash"),
    path('updateService/<int:service_id>',
         views.updateService, name="update-service-dash"),
    path('deleteService/<int:service_id>',
         views.deleteService, name="delete-service-dash"),

    # for Worker
    path('getWorker', views.getWorker, name="get-worker-dash"),
    path('postWorker', views.Worker_registration, name="post-worker-dash"),
    path('updateWorker/<int:Worker_id>',
         views.updateWorker, name="update-worker-dash"),
    path('deleteWorker/<int:Worker_id>',
         views.deleteWorker, name="delete-worker-dash"),

    # for profile
    path('getProfile', views.getProfile, name="get-profile-dash"),
    path('editBusiness', views.editBusiness, name="edit-business-dash"),
    path('editBusinessProfile', views.editBusinessProfile,
         name="edit-business-profile-dash"),
    path('updateProfile/<int:profile_id>',
         views.updateProfile, name="update-profile-dash"),

    path('changePassword', views.change_password, name='change-password-dash'),

    # For Hiring
    path('hirings/', views.BusinessHiringListView.as_view(),
         name='business-hiring-list'),
    path('hirings/approve/<int:id>', views.approve_business_hiring,
         name='approve-business-hiring'),
    path('hirings/complete/<int:id>', views.complete_business_hiring,
         name='complete-business-hiring'),
    path('hirings/reject/<int:id>', views.reject_business_hiring,
         name='reject-business-hiring'),

    # for notification
    path('api/notification/<int:notification_pk>',
         views.HireNotificationView.as_view(), name='business-hire-notification-api'),
    path('notifications/', views.AllNotificationPageView.as_view(),
         name="business-all-notification-page"),

]

app_name = 'adminbusiness'
