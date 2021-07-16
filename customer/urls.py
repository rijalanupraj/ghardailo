# External Import
from django.urls import path
from customer import views


# Internal Import

urlpatterns = [
path('customer-profile/', views.profileupdate, name="customerprofile"),

]
