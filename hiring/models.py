from django.db import models
from business.models import *
from customer.models import *

class Hiring(models.Model):
    business_service = models.ForeignKey(Business_Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = str(self.business_service) +"-->"+ str(self.customer)
        return name
