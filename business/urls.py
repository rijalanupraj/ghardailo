# External Import
from django.urls import path
from .import views

# Internal Import
from .views import(
    BusinessRegistartionCreateView
)


urlpatterns = [
    path('register/', BusinessRegistartionCreateView.as_view(),
         name='business-registration'),

    path('business-profile/', views.BusinessProfile, name='business-profile')
   
]
