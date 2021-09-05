from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators
from business.models import *

User = get_user_model()

class Worker(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, )
    picture = models.FileField(upload_to='img/worker')
    phone = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name