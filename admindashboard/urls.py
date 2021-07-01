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
    # <<====================Customer====================>>
    path('customer', views.customer),
    # <<====================Activities====================>>
    path('activities', views.activities),
]