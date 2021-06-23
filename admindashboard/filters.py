import django_filters
from django_filters import CharFilter
from service.models import *

class ServicesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    is_active = CharFilter(field_name='is_acitve', lookup_expr='icontains')
    class Meta:
        model = Services
        fields = ""
