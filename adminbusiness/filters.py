from business.models import Business_Service
import django_filters
from django_filters import CharFilter
from django_filters import BooleanFilter

from service.models import *

class ServicesFilter(django_filters.FilterSet):
     description = CharFilter(field_name='description', lookup_expr='icontains')
     class Meta:
        model = Business_Service
        fields = ""