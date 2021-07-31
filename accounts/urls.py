# External Import
from django.urls import path
from .views import(
    CustomerRegistrationCreateView,
    CustomerLoginView,
    BusinessRegistrationCreateView,
    BusinessLoginView
)
from django.contrib.auth import views as auth_views

# Internal Import
from . import views


urlpatterns = [
    path('register/', CustomerRegistrationCreateView.as_view(),
         name='customer-registration'),
    path('login/', CustomerLoginView.as_view(redirect_authenticated_user=True),
         name='customer-login'),
    path('mybusiness/register/', BusinessRegistrationCreateView.as_view(),
         name='business-registration'),
    path('mybusiness/login/', BusinessLoginView.as_view(), name="business-login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/',
         views.activate_account, name='email-activate'),


]
