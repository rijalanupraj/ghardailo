from django.forms import ModelForm
from business.models import *
from gallery.models import *
from worker.models import *
from customer.models import *
from service.models import *
from hiring.models import *
from review.models import *
from notification.models import *


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