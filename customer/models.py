from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    province = models.CharField(choices=PROVINCE_CHOICES, max_length=50)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " | " + self.user.username
