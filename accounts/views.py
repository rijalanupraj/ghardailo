# External Import
from django.shortcuts import render, redirect, HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.contrib.auth import login
from django.contrib import messages


# Internal Import
from .token_generator import account_activation_token

from django.contrib.auth import get_user_model
User = get_user_model()


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
        return redirect('customer-home')
    else:
        return HttpResponse('Activation link is invalid!')
