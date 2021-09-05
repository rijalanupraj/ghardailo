from django.urls import path, include
from . import views

urlpatterns = [
    # <<====================Dashboard====================>>
    path('dashboard', views.dashboard, name="my-admin-dashboard"),

    # <<====================Customer Registration====================>>
    path('cr', views.customer_registration),

    # <<====================Business Registration====================>>
    path('br', views.business_registration),

    # <<====================Administrator Registration====================>>
    path('ar', views.administrator_registration),

    # <<====================Service====================>>
    path('service', views.service),
    path('deleteservice/<int:service_id>', views.service_delete),
    path('updateservice/<int:service_id>', views.service_update),

    # <<====================Business====================>>
    path('business', views.business),
    path('business_active/<int:business_id>', views.business_active),
    path('business_inactive/<int:business_id>', views.business_inactive),
    path('business_verified/<int:business_id>', views.business_verified),
    path('business_not_verified/<int:business_id>', views.business_not_verified),
    path('viewbusiness/<int:business_id>', views.business_view, name="view-business"),
    path('change_hire_status1/<int:business_id>/<int:hire_id>', views.change_hire_status1),

    # <<====================Customer====================>>
    path('customer', views.customer, name="my-admin-customer-list-view"),
    path('customer_active/<int:customer_id>', views.customer_active),
    path('customer_inactive/<int:customer_id>', views.customer_inactive),
    path('viewcustomer/<int:customer_id>', views.customer_view, name="view-customer"),
    path('change_hire_status2/<int:customer_id>/<int:hire_id>', views.change_hire_status2),
]
