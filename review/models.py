from django.db import models
from django.core.validators import *
from customer.models import *
from business.models import *


class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=350, null=True)
    rating = models.FloatField(default=0, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
