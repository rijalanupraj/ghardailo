# Extrenal Import
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

# Internal Import
from django.contrib.auth import get_user_model
from .forms import BusinessRegistrationForm, BusinessLoginForm

User = get_user_model()


class BusinessRegistartionCreateView(CreateView):
    model = User
    form_class = BusinessRegistrationForm
    template_name = 'business/business-registration.html'
    success_url = reverse_lazy('customer-home')


class BusinessLoginView(auth_views.LoginView):
    form_class = BusinessLoginForm
    template_name = 'business/business-login.html'
