# External Import
from customer.models import Customer
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# Internal Import
from .models import Hiring
from business.models import Business_Service, Business
from service.models import Services
from customer.models import Customer


class CreateHireView(UserPassesTestMixin, View):

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        return True

    def post(self, request):
        business_id = request.POST['business-id']
        service_name = request.POST['service-select-form']
        message_text = request.POST['message-text']

        # Get Business
        business = Business.objects.get(id=business_id)

        # Get Service
        service = Services.objects.get(name=service_name)

        # Get Business Service
        business_service = Business_Service.objects.get(
            business=business, service=service)

        # Getting Customer
        user = request.user

        customer = Customer.objects.get(user=user)

        # Create New Hire
        # Hiring.objects.create(
        #     business_service=business_service, customer=customer, message_text=message_text)

        return redirect(request.META.get('HTTP_REFERER', 'customer-home'))
