from django.db import models
from django.core.validators import *
from customer.models import *
from business.models import *

class Review(models.Model):
    business=models.ForeignKey(Business, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    rating=models.IntegerField(default=0, validators=[MaxLengthValidator(5), MinLengthValidator(0)])

    def __str__(self):
        name = str(business)+"-->"+str(customer)
        return name
