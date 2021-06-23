from django.forms import ModelForm
from service.models import *

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'