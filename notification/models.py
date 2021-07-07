from django.db import models
from business.models import *
from customer.models import *

class Notification(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=100, null=True)
    read = models.BooleanField(default=False, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
