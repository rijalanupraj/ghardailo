from django.urls import path, include
from . import views

urlpatterns = [
    # <<====================Dashboard====================>>
    path('dashboard', views.dashboard, name='my-admin-dashboard'),

    # <<====================Customer Registration====================>>
    path('cr', views.customer_registration, name='customer-registration'),

    # <<====================Business Registration====================>>
    path('br', views.business_registration, name='business-registration'),

    # <<====================Administrator Registration====================>>
    path('ar', views.administrator_registration, name="staff-registration"),

    # <<====================Service====================>>
    path('service', views.service, name='service-list'),
    path('deleteservice/<int:service_id>',
         views.service_delete, name='service-delete'),
    path('updateservice/<int:service_id>',
         views.service_update, name='service-update'),

    # <<====================Business====================>>
    path('business', views.business, name='show-all-business'),
    path('business_active/<int:business_id>',
         views.business_active, name='make-business-active'),
    path('business_inactive/<int:business_id>',
         views.business_inactive, name='make-business-inactive'),
    path('business_verified/<int:business_id>',
         views.business_verified, name='verify-business'),
    path('business_not_verified/<int:business_id>',
         views.business_not_verified, name='unverify-business'),
    path('viewbusiness/<int:business_id>',
         views.business_view, name="view-business"),
    path('change_hire_status1/<int:business_id>/<int:hire_id>',
         views.change_hire_status1, name='change-hire-status'),

    # <<====================Customer====================>>
    path('customer', views.customer, name="my-admin-customer-list-view"),
    path('customer_active/<int:customer_id>',
         views.customer_active, name='make-customer-active'),
    path('customer_inactive/<int:customer_id>',
         views.customer_inactive, name='make-customer-inactive'),
    path('viewcustomer/<int:customer_id>',
         views.customer_view, name="view-customer"),
    path('change_hire_status2/<int:customer_id>/<int:hire_id>',
         views.change_hire_status2, name='change-hire-status-2'),
]

app_name = 'admindashboard'
