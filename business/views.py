# Extrenal Import
from django.shortcuts import render
from django.views.generic import CreateView

# Internal Import
from django.contrib.auth import get_user_model
from .forms import BusinessRegistrationForm

User = get_user_model()


class BusinessRegistartionCreateView(CreateView):
    model = User
    form_class = BusinessRegistrationForm
    template_name = 'business/business-registration.html'
