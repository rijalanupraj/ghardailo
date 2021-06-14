from django.db import models
from django.contrib.auth.models import User

PROVINCE_CHOICES = (
    ('Province 1', 'Province 1'),
    ('Province 2', 'Province 2'),
    ('Bagmati', 'Bagmati'),
    ('Gandaki', 'Gandaki'),
    ('Lumbini', 'Lumbini'),
    ('Karnali', 'Karnali'),
    ('Sudhurpachhim', 'Sudhurpachhim'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # many to one relation with user
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    province = models.CharField(choices=PROVINCE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)  # id generate by default
