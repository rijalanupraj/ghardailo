from django.db import models
from business.models import *
from customer.models import *

class Hiring(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        name = str(self.business)+"-->"+str(self.service)+"-->"+ str(self.customer)
        return name
