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
    path('business_verified/<int:business_id>', views.business_verified),
    path('business_not_verified/<int:business_id>', views.business_not_verified),
    path('viewbusiness/<int:business_id>', views.business_view),

    # <<====================Customer====================>>
    path('customer', views.customer, name="my-admin-customer-list-view"),
    path('viewcustomer/<int:customer_id>', views.customer_view),

    # <<====================Activities====================>>
    path('activities', views.activities),
]
