# External Import
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.db import transaction
from django.contrib.auth import login
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters


# For Email Verification
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site


# Internal Import
from .token_generator import account_activation_token
from . import forms
from . import utils
from django.contrib.auth import get_user_model
from customer.models import Customer
from business.models import Business
User = get_user_model()


class CustomerRegistrationCreateView(CreateView):
    model = User
    form_class = forms.CustomerRegistrationForm
    template_name = 'customer/customer-registration.html'
    success_url = reverse_lazy('customer-home')

    @method_decorator(sensitive_post_parameters('password1', 'password2'))
    def dispatch(self, request, *args, **kwargs):
        """
        Check the user is already logged in or not. If already logged in redirect them to specific pages.
        If not logged in then allow them to register to the site.

        """
        user = self.request.user
        if self.request.user.is_authenticated:
            if(user.is_customer):
                return redirect('customer-home')
            elif (user.is_business):
                return redirect('businessDash')
            elif (user.is_staff):
                return redirect('my-admin-dashboard')
            return redirect('customer-home')
        return super(CustomerRegistrationCreateView, self).dispatch(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_customer = True
        user.is_active = False
        user.email = form.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.name = form.cleaned_data.get('name')
        customer.phone = form.cleaned_data.get('phone')
        customer.province = form.cleaned_data.get('province')
        customer.city = form.cleaned_data.get('city')
        customer.street_address = form.cleaned_data.get('street_address')
        customer.save()

        current_site = get_current_site(self.request)
        utils.send_email_verification(current_site, user)
        messages.success(
            self.request, f'We have sent you an email, please confirm your email address to complete registration')
        return redirect('customer-login')


class BusinessRegistrationCreateView(CreateView):
    model = User
    form_class = forms.BusinessRegistrationForm
    template_name = 'business/business-registration.html'
    success_url = reverse_lazy('customer-home')

    @method_decorator(sensitive_post_parameters('password1', 'password2'))
    def dispatch(self, request, *args, **kwargs):
        """
        Check the user is already logged in or not. If already logged in redirect them to specific pages.
        If not logged in then allow them to register to the site.

        """
        user = self.request.user
        if self.request.user.is_authenticated:
            if(user.is_customer):
                return redirect('customer-home')
            elif (user.is_business):
                return redirect('businessDash')
            elif (user.is_staff):
                return redirect('my-admin-dashboard')
            return redirect('customer-home')
        return super(BusinessRegistrationCreateView, self).dispatch(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.is_business = True
        user.email = form.cleaned_data.get('email')
        user.save()
        business = Business.objects.create(user=user)
        business.name = form.cleaned_data.get('name')
        business.phone = form.cleaned_data.get('phone')
        business.province = form.cleaned_data.get('province')
        business.district = form.cleaned_data.get('district')
        business.city = form.cleaned_data.get('city')
        business.street_address = form.cleaned_data.get('street_address')
        business.is_solo = form.cleaned_data.get('is_solo')
        business.save()
        current_site = get_current_site(self.request)
        utils.send_email_verification(current_site, user)
        messages.success(
            self.request, f'We have sent you an email, please confirm your email address to complete registration')
        return redirect('business-login')


class CustomerLoginView(auth_views.LoginView):
    form_class = forms.CustomerLoginForm
    template_name = 'customer/customer-login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        if(self.request.user.is_customer):
            return reverse_lazy('customer-home')
        elif (self.request.user.is_business):
            return reverse_lazy('businessDash')
        elif (self.request.user.is_staff):
            return reverse_lazy('my-admin-dashboard')
        return super().get_success_url()


class BusinessLoginView(auth_views.LoginView):
    form_class = forms.BusinessLoginForm
    template_name = 'business/business-login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        if(self.request.user.is_customer):
            return reverse_lazy('customer-home')
        elif (self.request.user.is_business):
            return reverse_lazy('businessDash')
        elif (self.request.user.is_staff):
            return reverse_lazy('my-admin-dashboard')
        return super().get_success_url()


def activate_account(request, uidb64, token, backend='accounts.backends.EmailBackend'):
    """ Activate Account through email link """
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='accounts.backends.EmailBackend')
        messages.success(
            request, f'Your account has been activated successfully')
        # Redirect User to Their Respective Page (Customer/Business/Staff)
        if(user.is_customer):
            return redirect('customer-home')
        elif (user.is_business):
            return redirect('businessDash')
        elif (user.is_staff):
            return redirect('my-admin-dashboard')
        return redirect('customer-home')
    else:
        return HttpResponse('Activation link is invalid!')
