# External Import
from django.urls import path
from customer import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
#from .views import PasswordUpdateView


# Internal Import

urlpatterns = [
    path('customer-profile/', views.profileupdate, name="customerprofile"),
    path('change-password/', views.change_password, name='change_password'),
    path('hirings/', views.CustomerHiringPageView.as_view(),
         name="customer-hiring-page"),
    path('hirings/delete/<pk>/', views.CustomerHiringDeleteView.as_view(),
         name='customer-hiring-delete-view'),

]

# App Name
app_name = 'customer'
