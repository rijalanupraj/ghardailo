# External Improt
from customer.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

# Internal Import
from .models import Customer, PROVINCE_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomerRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    province = forms.ChoiceField(choices=PROVINCE_CHOICES)
    city = forms.CharField(max_length=200, required=True)
    street_address = forms.CharField(max_length=200, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.name = self.cleaned_data.get('name')
        customer.phone = self.cleaned_data.get('phone')
        customer.province = self.cleaned_data.get('province')
        customer.city = self.cleaned_data.get('city')
        customer.locality = self.cleaned_data.get('street_address')
        customer.save()
        return user
