from django.db import models

# Create your models here.


class Business(models.Model):
  
  name=models.CharField(max_length=50)
  logo= models.ImageField()
  cover_picture= models.ImageField()
  district= models.CharField(max_length=100)
  province=models.CharField(max_length=100)
  is_business= models.BooleanField(default=false)
  tole= models.CharField(max_length=100)
  description= models.TextField()
  phone= models.CharField(max_length=50)
  email= models.CharField(max_length=50)



