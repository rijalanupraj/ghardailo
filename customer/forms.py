# External Improt
from customer.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.urls import reverse


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

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        user = User.objects.filter(email=email)
        if user:
            self.add_error('email', 'User with this Email already exists.')


class LoginForm(AuthenticationForm):

    class Meta:
        model = User

    def confirm_login_allowed(self, user):
        if not user.is_active:
            print("User is not active")
