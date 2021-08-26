from django.forms import ModelForm
from django.forms.widgets import PasswordInput
from business.models import *
from gallery.models import *
from worker.models import *
from customer.models import *
from service.models import *
from hiring.models import *
from review.models import *
from notification.models import *
from accounts.models import User
from django import forms


class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = "__all__"


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"


class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'


class BusinessServicesForm(ModelForm):
    class Meta:
        model = Business_Service
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class HiringForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'


class StaffUserCreationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',
                  'is_admin', 'is_superuser')


class CustomerCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
