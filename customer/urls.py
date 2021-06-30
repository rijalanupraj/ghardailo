# External Import
from django.urls import path
from django.contrib.auth import views as auth_views


# Internal Import
from .views import(
    CustomerRegistartionCreateView,
    CustomerLoginView,
)


urlpatterns = [
    path('register/', CustomerRegistartionCreateView.as_view(),
         name='customer-registration'),
    path('login/', CustomerLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
