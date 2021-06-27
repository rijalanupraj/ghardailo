# External Improt
from customer.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

# Internal Import
from .models import Business, PROVINCE_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()


class BusinessRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    province = forms.ChoiceField(choices=PROVINCE_CHOICES)
    district = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=200, required=True)
    street_address = forms.CharField(max_length=200, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        user = User.objects.filter(email=email)
        if user:
            self.add_error('email', 'User with this Email already exists.')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_business = True
        user.email = self.cleaned_data.get('email')
        user.save()
        business = Business.objects.create(user=user)
        business.name = self.cleaned_data.get('name')
        business.phone = self.cleaned_data.get('phone')
        business.province = self.cleaned_data.get('province')
        business.district = self.cleaned_data.get('district')
        business.city = self.cleaned_data.get('city')
        business.street_address = self.cleaned_data.get('street_address')
        business.save()
        return user
