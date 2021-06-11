from django.urls import path
from Customer import views


urlpatterns = [
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
]