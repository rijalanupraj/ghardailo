# External Import
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views as auth_views
from django.db import transaction
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Internal Import

from django import forms
from .forms import CustomerUpdateForm
from hiring.models import Hiring
from django.contrib.auth import get_user_model
from .models import Customer

User = get_user_model()


# @login_required(login_url='/')

def profileupdate(request):
    cu_form = CustomerUpdateForm

    if request.method == 'POST':

        cu_form = CustomerUpdateForm(
            request.POST, request.FILES, instance=request.user.customer)

        if cu_form.is_valid():
            cu_form.save()
            messages.success(
                request, f' Your Account Has Been Successfully Updated')
            return redirect('customerprofile')

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
            return redirect('change_password')
        else:
            messages.error(
                request, 'Invalid Password. Retype Your Password Correctly')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'customer/changepassword.html', {
        'form': form
    })
