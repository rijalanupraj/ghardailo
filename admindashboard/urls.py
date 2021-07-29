from django.urls import path, include
from . import views 

urlpatterns = [
    # <<====================Dashboard====================>>
    path('dashboard', views.dashboard),

    # <<====================Service====================>>
    path('service', views.service),
    path('deleteservice/<int:service_id>', views.service_delete),
    path('updateservice/<int:service_id>', views.service_update),

    # <<====================Business====================>>
    path('business', views.business),
    path('viewbusiness/<int:business_id>', views.business_view),

    # <<====================Customer====================>>
    path('customer', views.customer),
    path('viewcustomer/<int:customer_id>', views.customer_view),

    # <<====================Activities====================>>
    path('activities', views.activities),
]