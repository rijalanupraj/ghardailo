# External Improt
from django import forms
from .models import Worker

class WorkerProfileForm(forms.ModelForm):
    class Meta:
     model=Worker
     fields= '__all__'
    