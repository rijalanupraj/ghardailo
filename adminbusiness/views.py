from django.contrib import messages
from .forms import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# internal input
from business.models import Business
from django.shortcuts import redirect, render
from business.models import *
from gallery.models import *
from worker.models import *
from customer.models import *
from service.models import *
from hiring.models import *
from review.models import *
from notification.models import *

# Create your views here.

def businessDashboard(request):
    user=request.user
    business=Business.objects.get(user=user)
    gallery = Gallery.objects.all()
    business_service = Business_Service.objects.all()
    business_service_count = Business_Service.objects.all().count()
    worker = Worker.objects.all()
    worker_count = Worker.objects.all().count()
    customer = Customer.objects.all()
    customer_count = Customer.objects.all().count()
    hiring = Hiring.objects.all()
    hiring_count = Hiring.objects.all().count()
    review = Review.objects.all()
    review_count = Review.objects.all().count()

    context={
        'business':business,
        'gallery':gallery,
        'business_service':business_service,
        'business_service_count':business_service_count,
        'worker':worker,
        'worker_count':worker_count,    
        'customer':customer,
        'customer_count':customer_count,
        'hiring':hiring,
        'hiring_count':hiring_count,
        'review':review,
        'review_count':review_count,
    }

    return render(request, 'adminbusiness/base/dashboard.html', context)




def getService(request):
    businessService = Business_Service.objects.filter(business=request.user.business)

    context = {
        'businessService': businessService,

    }
    return render(request, 'adminbusiness/base/show-service.html', context)

def postService(request):
    if request.method == 'POST':

        form = BusinessServicesForm(request.POST, request.FILES)
        if form.is_valid():
            businessService = Business_Service.objects.filter(business=request.user.business)
            
            obj=form.save(commit=False)
            already_exist=True
            for ser in businessService:
                if ser.service==obj.service:
                    already_exist=False
            if already_exist:
                obj.business=request.user.business
                obj.save()
                messages.add_message(request, messages.SUCCESS, 'Service Added Successfully') 
            return redirect('getServiceDash')
        else:
            messages.add_message(request, messages.ERROR, 'Error adding service')
            return render(request, 'adminbusiness/base/post-service.html')
    else:
        form = BusinessServicesForm()

    context={
        'form':form
    }

    return render(request, 'adminbusiness/base/post-service.html', context)

def updateService(request, service_id):
    instance = Business_Service.objects.get(id=service_id)
    if request.method == "POST":
        form = BusinessServicesForm1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/b/getService')
    context = {
        'form': BusinessServicesForm1(instance=instance),
        'service':instance
    }
    return render(request, 'adminbusiness/base/update-service.html', context)

def deleteService(request, service_id):
    service = Business_Service.objects.get(id=service_id)
    service.delete()
    return redirect('getServiceDash')





#for profile
def getProfile(request):
    profile=Business_Profile.object.all()

    context={
        'profile':profile
    }
    return render(request, 'adminbusiness/base/show-profile.html',context)

def editBusiness(request):
    if request.method == 'POST':
        form = EditBusinessForm(
            request.POST, request.FILES, instance=request.user.business)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Service Added Successfully')
            # return redirect('getProfileDash')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error adding service')
    else:
        form = EditBusinessForm(
            instance=request.user.business)
    context = {
        'form': form
    }
    return render(request, 'adminbusiness/base/edit-business.html', context)

def editBusinessProfile(request):
    if request.method == 'POST':
        form = BusinessProfileForm(
            request.POST, request.FILES, instance=request.user.business.business_profile)
        form1 = BusinessProfileForm1(
            request.POST, request.FILES, instance=request.user.business)
        if form.is_valid():
            form.save()
            form1.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Service Added Successfully')
            # return redirect('getProfileDash')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error adding service')
    else:
        form = BusinessProfileForm(
            instance=request.user.business.business_profile)
        form1 = BusinessProfileForm1(
            instance=request.user.business)
    context = {
        'form': form,
        'form1':form1
    }
    return render(request, 'adminbusiness/base/post-profile.html', context)

def updateProfile(request, profile_id):
    instance = Business_Profile.objects.get(id=profile_id)
    if request.method == "POST":
        form = BusinessProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/b/getProfile')
    context = {
        'form': BusinessProfileForm(instance=instance),
    }
    return render(request, 'adminbusiness/base/update-profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changePasswordDash')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'adminbusiness/base/change-password.html', {
        'form': form
    })