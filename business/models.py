from django.db.models.fields.files import ImageField
from django.db.models.signals import pre_save, post_save
from django.db import models
from django.contrib.auth import get_user_model
from service.models import *
from .utils import unique_slug_generator
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
    slug = models.SlugField(unique=True, blank=True, null=True)
    cover_picture = models.ImageField(blank=True, null=True)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    is_solo = models.BooleanField(default=False)
    street_address = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=50)
    is_verified = models.BooleanField()
    contact_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name + " | " + self.user.username


# This is done to create unique slug for the business
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance)


# Connecting pre_save_receiver function and sender Post
pre_save.connect(post_pre_save_receiver, sender=Business)


class Business_Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        name = str(self.business)+"-->"+str(self.service)
        return name


Language_CHOICES = (
    ('Nepali', 'Nepali'),
    ('English', 'English'),
)


class Business_Profile(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE)
    # Business_Service=models.OneToManyField(Business_Service)
    intro = models.TextField(null=True)
    established = models.DateField(null=True)
    founder = models.CharField(max_length=30, null=True)
    moto = models.CharField(max_length=100, null=True)
    language = models.CharField(
        choices=Language_CHOICES, max_length=100, null=True)
    experience_year = models.IntegerField(null=True)
    service_provided = models.IntegerField(null=True)
    happy_customers = models.IntegerField(null=True)
    Awards_won = models.IntegerField(null=True)


def create_business_profile(sender, instance, created, **kwargs):
    if created:
        Business_Profile.objects.create(business=instance)


# This Creates the business profile once business is created
post_save.connect(create_business_profile, sender=Business)
