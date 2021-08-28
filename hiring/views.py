# External Import
from customer.models import Customer
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib import messages
from django.urls import reverse

# Internal Import
from .models import Hiring
from business.models import Business_Service, Business
from service.models import Services
from customer.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()


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
        user = User.objects.get(id=request.user.id)
        customer = user.customer

        # Create New Hire
        Hiring.objects.create(
            business_service=business_service, customer=customer, message=message_text)

        slug_of_current_business = request.build_absolute_uri(
            reverse('business-profile', args=(business.slug, )))
        print(slug_of_current_business)
        messages.success(
            request, f'You have successfully requested <a href="{slug_of_current_business}">{business.name}</a> for {service} service. Thank You 🙏')

        return redirect(request.META.get('HTTP_REFERER', 'customer-home'))
