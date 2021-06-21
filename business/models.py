from django.db import models
from django.contrib.auth import get_user_model
from service.models import *

User = get_user_model()

class Business(models.Model):
  PROVINCE_CHOICES = (
    ('Province 1', 'Province 1'),
    ('Province 2', 'Province 2'),
    ('Bagmati', 'Bagmati'),
    ('Gandaki', 'Gandaki'),
    ('Lumbini', 'Lumbini'),
    ('Karnali', 'Karnali'),
    ('Sudhurpachhim', 'Sudhurpachhim'),
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name=models.CharField(max_length=50)
  logo= models.ImageField(blank=True, null=True)
  cover_picture= models.ImageField(blank=True, null=True)
  district= models.CharField(max_length=100)
  province=models.CharField(choices=PROVINCE_CHOICES, max_length=100)
  is_business= models.BooleanField(default=False)
  tole= models.CharField(max_length=100)
  description= models.TextField()
  phone= models.CharField(max_length=50)
  email= models.CharField(max_length=50)

  def __str__(self):
        return self.name +" | "+ self.user.username


class Business_Service(models.Model):
  business = models.ForeignKey(Business, on_delete=models.CASCADE)
  service = models.ForeignKey(Services, on_delete=models.CASCADE)
  description = models.TextField(max_length=500, blank=True, null=True)

  def __str__(self):
    name = str(self.business)+"-->"+str(self.service)
    return name


