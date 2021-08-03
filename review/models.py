from django.db import models
from django.core.validators import *
from customer.models import *
from business.models import *

class Review(models.Model):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    rating_status = (
        (zero, 0),
        (one, 1),
        (two, 2),
        (three, 3),
        (four, 4),
        (five, 5)
    )
    business=models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    comment=models.CharField(max_length=200, null=True)
    rating=models.IntegerField(choices=rating_status, default=zero, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
