from django.shortcuts import render
from .forms import WorkerProfileForm
from django.contrib import messages
from .models import *

def getProfile(request, worker_id):
    profile = Worker.objects.get(id=worker_id)

    context = {
        'profile':profile,
    }
    return render(request, 'worker/wprofile.html', context)

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
