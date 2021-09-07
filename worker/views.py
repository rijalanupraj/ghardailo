from django.shortcuts import render, redirect
from .forms import WorkerProfileForm
from django.contrib import messages
from .models import *


from django.contrib import messages
from django.urls.base import reverse_lazy
import random
import string
import datetime
from .forms import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DeleteView,
    View
)

from hiring.models import *


def workerDashboard(request):
    hiring_completed = Hiring.objects.filter(
        worker=request.user.worker, status='CO').count()

    hiring_onhold = Hiring.objects.filter(
        worker=request.user.worker, status='AC').count()

    context = {
        'hiring_completed': hiring_completed,
        'hiring_onhold': hiring_onhold,
    }
    return render(request, 'worker/base/worker-dashboard.html', context)


def getProfile(request, worker_id):
    profile = Worker.objects.get(id=worker_id)

    context = {
        'profile': profile,
    }
    return render(request, 'worker/main/wprofile.html', context)

# def profileupdate(request):
#     cu_form = WorkerProfileForm

#     if request.method == 'POST':

#         cu_form = WorkerProfileForm(
#             request.POST, request.FILES, instance=request.user.customer)
#         print(cu_form)

#         if cu_form.is_valid():
#             cu_form.save()
#             messages.success(
#                 request, f' Your Account Has Been Successfully Updated')
#             return redirect('customer:customerprofile')

#     else:

#         cu_form = WorkerProfileForm(instance=request.user.customer)

#     # Hiring Part
#     customer_hire = Hiring.objects.filter(
#         customer=request.user.customer).order_by('-date_time')
#     context = {
#         'cu_form': cu_form,
#         'customer_hire': customer_hire,
#     }

#     return render(request, 'customer/customerprofile.html', context)


class WorkerHiringListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "worker/base/worker-hiring-display.html"

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_worker
        return False

    def get_queryset(self):
        return Hiring.objects.filter(
            worker=self.request.user.worker).order_by('-date_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def complete_worker_hiring(request, id):
    hiring = Hiring.objects.get(id=id)
    hiring.status = 'CO'
    hiring.save()
    customer = hiring.customer
    business_service = hiring.business_service
    # # Notification Part
    # notification_message = f"approved your hire request for {business_service.service.name} service"
    # Notification.objects.create(
    #     to_user=customer.user, from_user=request.user, title="Approved Hire Request", message=notification_message, business_service=business_service)
    return redirect('worker:worker-hiring-list')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('changePasswordDash')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'worker/base/change-password.html', {
        'form': form
    })
    return redirect('worker:worker-dashboard')


def editWorker(request):
    if request.method == 'POST':
        form = EditWorkerForm(
            request.POST, request.FILES, instance=request.user.worker)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Service Added Successfully')
            return redirect('worker:worker-dashboard')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error adding service')
    else:
        form = EditWorkerForm(
            instance=request.user.worker)
    context = {
        'form': form
    }
    return render(request, 'worker/base/edit-worker.html', context)
