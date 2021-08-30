from django.db import models
from django.core.validators import *
from customer.models import *
from business.models import *


class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=350, null=True)
    rating = models.FloatField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.business.name)+" | "+str(self.customer.name)
