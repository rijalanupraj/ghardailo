import django_filters
from django_filters import CharFilter
from django_filters import BooleanFilter

from business.models import *
from gallery.models import *
from worker.models import *
from customer.models import *
from service.models import *
from hiring.models import *
from wcb.models import *
from review.models import *
from notification.models import *

class ServicesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    is_active = BooleanFilter(field_name='is_active', lookup_expr=None)
    class Meta:
        model = Services
        fields = ""

class BusinessFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Business
        fields = ""

class GalleryFilter(django_filters.FilterSet):
    business = CharFilter(field_name='business', lookup_expr='exact', queryset=Business.objects.all())
    class Meta:
        model = Gallery
        fields = ""

class WorkerFilter(django_filters.FilterSet):
    business = CharFilter(field_name='business', lookup_expr='exact', queryset=Business.objects.all())
    name = CharFilter(field_name='name', lookup_expr='icontains')
    is_active = BooleanFilter(field_name='is_active', lookup_expr=None)
    class Meta:
        model = Worker
        fields = ""

class BusinessServiceFilter(django_filters.FilterSet):
    business = CharFilter(field_name='business', lookup_expr='exact', queryset=Business.objects.all())
    service = CharFilter(field_name='service', lookup_expr='exact', queryset=Services.objects.all())
    class Meta:
        model = Business_Service
        fields = ""

class CustomerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    province = CharFilter(field_name='province', lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = ""

class HiringFilter(django_filters.FilterSet):
    business_service = CharFilter(field_name='business_service', lookup_expr='exact', queryset=Business_Service.objects.all())
    customer = CharFilter(field_name='customer', lookup_expr='exact', queryset=Customer.objects.all())
    class Meta:
        model = Hiring
        fields = ""

class WCBFilter(django_filters.FilterSet):
    hiring = CharFilter(field_name='hiring', lookup_expr='exact', queryset=Hiring.objects.all())
    worker = CharFilter(field_name='worker', lookup_expr='exact', queryset=Worker.objects.all())
    class Meta:
        model = WCB
        fields = ""

class ReviewFilter(django_filters.FilterSet):
    business = CharFilter(field_name='business', lookup_expr='exact', queryset=Business.objects.all())
    customer = CharFilter(field_name='customer', lookup_expr='exact', queryset=Customer.objects.all())
    class Meta:
        model = Review
        fields = ""

class NotificationFilter(django_filters.FilterSet):
    business = CharFilter(field_name='business', lookup_expr='exact', queryset=Business.objects.all())
    customer = CharFilter(field_name='customer', lookup_expr='exact', queryset=Customer.objects.all())
    class Meta:
        model = Notification
        fields = ""