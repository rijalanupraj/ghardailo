from django.db import models
from business.models import *
from customer.models import *


class Hiring(models.Model):
    PENDING = 'PE'
    ACCEPTED = 'AC'
    REJECTED = 'RE'
    CANCEL = 'CA'
    COMPLETED = 'CO'
    HIRE_STATUS = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (CANCEL, 'Cancel'),
        (COMPLETED, 'Completed'),
    ]

    business_service = models.ForeignKey(
        Business_Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    status = models.CharField(
        max_length=20, choices=HIRE_STATUS, default=PENDING)

    def __str__(self):
        name = str(self.business_service) + "-->" + str(self.customer)
        return name
