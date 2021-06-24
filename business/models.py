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


class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True)
    cover_picture = models.ImageField(blank=True, null=True)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    is_solo = models.BooleanField(default=False)
    street_address = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " | " + self.user.username
