from django.db import models
from django.contrib.auth import get_user_model
from service.models import *

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


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to="images/")
    cover_picture = models.ImageField(blank=True, null=True, upload_to="images/")
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100, choices=PROVINCE_CHOICES, null=True)
    is_solo = models.BooleanField(default=False)
    street_address = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " | " + self.user.username


class Business_Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        name = str(self.business)+"-->"+str(self.service)
        return name
