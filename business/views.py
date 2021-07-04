# Extrenal Import
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
from django.urls import reverse_lazy

# Internal Import
from django.contrib.auth import get_user_model
from .forms import BusinessRegistrationForm
from .models import Business
User = get_user_model()


class BusinessRegistartionCreateView(CreateView):
    model = User
    form_class = BusinessRegistrationForm
    template_name = 'business/business-registration.html'
    success_url = reverse_lazy('customer-home')


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
