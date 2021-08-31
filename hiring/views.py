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
from django.contrib.auth import get_user_model
from notification.models import Notification

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

        # Notification Part
        notification_message = f"{user.customer.name} requested for service {service.name} "
        Notification.objects.create(
            to_user=business.user, from_user=user, title="Hire Request", message=notification_message, business_service=business_service)

        return redirect(request.META.get('HTTP_REFERER', 'customer-home'))
