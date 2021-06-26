# Extrenal Import
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Internal Import
from django.contrib.auth import get_user_model
from .forms import CustomerRegistrationForm
User = get_user_model()


class CustomerRegistartionCreateView(CreateView):
    model = User
    form_class = CustomerRegistrationForm
    template_name = 'customer/customer-registration.html'
    success_url = reverse_lazy('customer-home')
