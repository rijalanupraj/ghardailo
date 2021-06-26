# External Import
from django.urls import path

# Internal Import
from .views import(
    CustomerRegistartionCreateView
)


urlpatterns = [
    path('register/', CustomerRegistartionCreateView.as_view(),
         name='customer-registration'),
]
