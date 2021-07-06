from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from business.models import *
from gallery.models import *
from worker.models import *
from customer.models import *
from service.models import *
from hiring.models import *
from wcb.models import *
from review.models import *
from notification.models import *

from .forms import *
from .filters import *

# <<====================Dashboard====================>>
def dashboard(request):
    user = User.objects.all().count()
    service = Services.objects.all().count()
    business = Business.objects.all().count()
    gallery = Gallery.objects.all().count()
    business_service = Business_Service.objects.all().count()
    worker = Worker.objects.all().count()
    customer = Customer.objects.all().count()
    hiring = Hiring.objects.all().count()
    review = Review.objects.all().count()
    notification = Notification.objects.all().count()

    dictionary = {
        'user': user,
        'service': service,
        'business': business,
        'gallery': gallery,
        'worker': worker,
        'business_service': business_service,
        'customer': customer,
        'hiring': hiring,
        'review': review,
        'notification': notification,
        'dashboard': 'selected'
    }
    return render(request, 'admindashboard/dashboard.html', dictionary)

# <<====================Service====================>>
def service(request):
    service = Services.objects.all()
    service_filter = ServicesFilter(request.GET, queryset=service)
    service_final = service_filter.qs

    form  = ServicesForm
    if request.method == "POST":
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'New service has been added to GharDailo.')
            return redirect('/a/service')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to add service, please try again!!!')
            return render(request, 'admindashboard/servie.html', {'form':form, 'service_filter':service_filter}) 
    dictionary = {'services':service_final, 'service_filter':service_filter, 'form': form, 'BTM':'Add', 'service': 'selected'}
    return render(request, 'admindashboard/service.html', dictionary)

def service_delete(request, service_id):
    service = Services.objects.get(id=service_id)
    service_name = service.name
    service.delete()    
    messages.add_message(request, messages.SUCCESS, "'"+service_name+ "'"+' service has been removed.')
    return redirect('/a/service')

def service_update(request, service_id):
    service = Services.objects.all()
    service_filter = ServicesFilter(request.GET, queryset=service)
    service_final = service_filter.qs

    particular_service = Services.objects.get(id=service_id)
    form  = ServicesForm(instance=particular_service)
    if request.method == "POST":
        form = ServicesForm(request.POST, instance=particular_service)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Service has been updated.')
            return redirect('/a/service')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to update service, please try again!!!')
            return render(request, 'admindashboard/servie.html', {'form':form, 'service_filter':service_filter}) 
    dictionary = {'services':service_final, 'service_filter':service_filter, 'form': form, 'BTM':'Update', 'service': 'selected'}
    return render(request, 'admindashboard/service.html', dictionary)


# <<====================Business====================>>
def business(request):
    dictionary = {'business': 'selected'}
    return render(request, 'admindashboard/business.html', dictionary)

# <<====================Customer====================>>
def customer(request):
    dictionary = {'customer': 'selected'}
    return render(request, 'admindashboard/customer.html', dictionary)

# <<====================Activities====================>>
def activities(request):
    dictionary = {'activities': 'selected'}
    return render(request, 'admindashboard/activities.html', dictionary)