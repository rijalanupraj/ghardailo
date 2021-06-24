# External Import
from django.urls import path

# Internal Import
from .views import(
    BusinessRegistartionCreateView
)


urlpatterns = [
    path('register/', BusinessRegistartionCreateView.as_view(),
         name='business-registration'),
]
