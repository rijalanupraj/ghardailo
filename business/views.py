
# Extrenal Import
from business.models import Business_Profile, Business
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Internal Import

# anup, samir, shankahr (people) - listview
# samir - detail view


class BusinessProfileView(DetailView):
    queryset = Business.objects.all()
    template_name = "business/business-profile.html"
    slug_url_kwarg = 'slug'
