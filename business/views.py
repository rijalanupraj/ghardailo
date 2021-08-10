from worker.models import Worker
from business.models import Business
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from worker.models import *

class BusinessListPageView(UserPassesTestMixin, ListView):
    template_name = "business/business-list-page.html"

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_customer
        return True

    # Redirect user to who doesn't have permission to access this page
    def handle_no_permission(self):
        if self.request.user.is_business:
            return redirect('businessDash')
        elif self.request.user.is_staff:
            return redirect('my-admin-dashboard')
        return redirect('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query is not None:
            context["query"] = query
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None and query != '':
            return Business.objects.search(query).active().distinct()
        return Business.objects.all()


class BusinessProfileView(UserPassesTestMixin, DetailView):
    queryset = Business.objects.all()
    template_name = "business/business-profile.html"
    slug_url_kwarg = 'slug'

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_customer
        return True

    # Redirect user to who doesn't have permission to access this page
    def handle_no_permission(self):
        if self.request.user.is_business:
            return redirect('businessDash')
        elif self.request.user.is_staff:
            return redirect('my-admin-dashboard')
        return redirect('home-page')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        worker=Worker.objects.filter(business__slug=slug)
        context["Worker"] = worker
        return context
