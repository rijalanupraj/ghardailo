from django.db import models
from django.core import validators
from business.models import *

class Worker(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    picture = models.FileField(upload_to='media/img/worker')
    phone = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)])
    is_active = models.BooleanField()

    def __str__(self):
        return self.name