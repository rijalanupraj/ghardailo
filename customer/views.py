# Extrenal Import
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.db import transaction


# For Email Verification
from accounts.token_generator import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

# Internal Import
from django.contrib.auth import get_user_model
from .forms import CustomerRegistrationForm, LoginForm
from .models import Customer
User = get_user_model()


class CustomerRegistartionCreateView(CreateView):
    model = User
    form_class = CustomerRegistrationForm
    template_name = 'customer/customer-registration.html'
    success_url = reverse_lazy('customer-home')

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
        email_subject = 'Activate Your Account'
        message = render_to_string('accounts/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()
        messages.success(
            self.request, f'We have sent you an email, please confirm your email address to complete registration')
        return redirect('customer-login')


class CustomerLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'customer/customer-login.html'
