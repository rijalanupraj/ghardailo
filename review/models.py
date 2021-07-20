from django.db import models
from django.core.validators import *
from customer.models import *
from business.models import *

class Review(models.Model):
    rating_status = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    business=models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    comment=models.CharField(max_length=200, null=True)
    rating=models.IntegerField(default=0, choices=rating_status, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
