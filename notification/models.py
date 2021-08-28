from django.db import models
from business.models import *
from customer.models import *
from django.utils import timezone


class Notification(models.Model):
    to_user = models.ForeignKey(
        User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(
        User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=255, null=True)
    has_seen = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(default=timezone.now)
