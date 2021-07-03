# External Import
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

# Internal Import
from .token_generator import account_activation_token


def send_email_verification(current_site, user):
    email_subject = 'Activate Your Account'
    message = render_to_string('accounts/activate_account.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    email = EmailMessage(email_subject, message, to=[user.email])
    email.send()
