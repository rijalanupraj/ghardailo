# Extrenal Import
from business.models import Business
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Internal Import
from .models import Business


class BusinessListPageView(UserPassesTestMixin, ListView):
    template_name = "business/business-list-page.html"

    # For Future Use
    def test_func(self):
        # if self.request.user.is_authenticated:
        #     return not self.request.user.is_staff
        return True

    # def handle_no_permission(self):
    #     return redirect('where you want to redirect')

    def get_queryset(self):
        request = self.request
        return Business.objects.all()
