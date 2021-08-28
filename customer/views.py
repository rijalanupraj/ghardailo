# External Import
from bookmark.models import Bookmark
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views as auth_views
from django.db import transaction
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DeleteView,
)
import json
from django.contrib.auth.decorators import login_required

# Internal Import

from django import forms
from .forms import CustomerUpdateForm
from hiring.models import Hiring
from django.contrib.auth import get_user_model
from .models import Customer
from business.models import Business
from .decorators import customer_only
from business.models import Business

User = get_user_model()


# @login_required(login_url='/')

def profileupdate(request):
    cu_form = CustomerUpdateForm

    if request.method == 'POST':

        cu_form = CustomerUpdateForm(
            request.POST, request.FILES, instance=request.user.customer)
        print(cu_form)

        if cu_form.is_valid():
            cu_form.save()
            messages.success(
                request, f' Your Account Has Been Successfully Updated')
            return redirect('customer:customerprofile')

    else:

        cu_form = CustomerUpdateForm(instance=request.user.customer)

    # Hiring Part
    customer_hire = Hiring.objects.filter(
        customer=request.user.customer).order_by('-date_time')
    context = {
        'cu_form': cu_form,
        'customer_hire': customer_hire,
    }

    return render(request, 'customer/customerprofile.html', context)


# For password change

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password Has Updated Successfully')
            return redirect('customer:customerprofile')
        else:
            messages.error(
                request, 'Invalid Password. Retype Your Password Correctly')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'customer/changepassword.html', {
        'form': form
    })


class CustomerHiringPageView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "customer/customer-hiring-display.html"

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_customer
        return False

    def get_queryset(self):
        return Hiring.objects.filter(
            customer=self.request.user.customer).order_by('-date_time')


class CustomerHiringDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hiring
    success_url = reverse_lazy('customer:customer-hiring-page')

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_customer:
            self.object = self.get_object()
            if self.object.customer == self.request.user.customer:
                return True
        return False

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class CustomerBusinessBookmarkListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "customer/customer-bookmark-display.html"

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_customer
        return False

    def get_queryset(self):
        return Bookmark.objects.filter(
            customer=self.request.user.customer).order_by('-date_time')


class CustomerBookmarkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('customer:customer-bookmark-page')

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_customer:
            self.object = self.get_object()
            if self.object.customer == self.request.user.customer:
                return True
        return False

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@login_required
@customer_only
def business_bookmark_toggle_for_customer(request, slug):
    if request.user.is_staff:
        return HttpResponse("Forbidden")

    current_customer = request.user.customer
    business = Business.objects.get(slug=slug)

    is_bookmarked = False
    current_bookmark = Bookmark.objects.filter(
        customer=current_customer, business=business)
    if current_bookmark:
        current_bookmark.delete()
    else:
        Bookmark.objects.create(
            customer=current_customer, business=business)
        is_bookmarked = True

    resp = {
        "isBookmarked": is_bookmarked,
    }

    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")
