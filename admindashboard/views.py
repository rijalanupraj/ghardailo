from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from business.models import *
from gallery.models import *
from worker.models import *
from customer.models import *
from service.models import *
from hiring.models import *
from review.models import *
from notification.models import *
from bookmark.models import *

from .forms import *
from .filters import *

# <<====================Dashboard====================>>


def dashboard(request):
    user = User.objects.all().count()
    admin = User.objects.filter(is_staff=True).all().count()
    service = Services.objects.all().count()
    business = Business.objects.all().count()
    gallery = Gallery.objects.all().count()
    business_service = Business_Service.objects.all().count()
    worker = Worker.objects.all().count()
    customer = Customer.objects.all().count()
    hiring = Hiring.objects.all().count()
    review = Review.objects.all().count()
    notification = Notification.objects.all().count()
    bookmark = Bookmark.objects.all().count()

    dictionary = {
        'user': user,
        'admin': admin,
        'service': service,
        'business': business,
        'gallery': gallery,
        'worker': worker,
        'business_service': business_service,
        'customer': customer,
        'hiring': hiring,
        'review': review,
        'notification': notification,
        'bookmark': bookmark,
        'dashboard': 'selected'
    }
    return render(request, 'admindashboard/dashboard.html', dictionary)

# <<====================Customer Registration====================>>


def customer_registration(request):
    dictionary = {
        'dashboard': 'selected'
    }
    return render(request, 'admindashboard/Customer_Registration.html', dictionary)


# <<====================Business Registration====================>>
def business_registration(request):
    dictionary = {
        'dashboard': 'selected'
    }
    return render(request, 'admindashboard/Business_Registration.html', dictionary)


# <<====================Administration Registration====================>>
def administrator_registration(request):
    u_form = StaffUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if u_form.is_valid():
            password = u_form.cleaned_data['password']
            user = u_form.save(commit=False)
            user.is_staff = True
            user.is_active = True
            user.set_password(password)
            user.save()
            messages.success(
                request, f'{user.username} staff user has been created')
            return redirect('my-admin-dashboard')
    context = {
        'u_form': u_form,
        'dashboard': 'selected'
    }
    return render(request, 'admindashboard/Administrator_Registration.html', context)


# <<====================Service====================>>
def service(request):
    service = Services.objects.all()
    service_filter = ServicesFilter(request.GET, queryset=service)
    service_final = service_filter.qs

    form = ServicesForm
    if request.method == "POST":
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'New service has been added to GharDailo.')
            return redirect('/a/service')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Failed to add service, please try again!!!')
            return render(request, 'admindashboard/servie.html', {'services': service_final, 'service_filter': service_filter, 'form': form, 'BTM': 'Add', 'service': 'selected'})
    dictionary = {
        'services': service_final,
        'service_filter': service_filter,
        'form': form,
        'BTM': 'Add',
        'service': 'selected'
    }

    return render(request, 'admindashboard/service.html', dictionary)


def service_delete(request, service_id):
    service = Services.objects.get(id=service_id)
    service_name = service.name
    service.delete()
    messages.add_message(request, messages.SUCCESS, "'" +
                         service_name + "'"+' service has been removed.')
    return redirect('/a/service')


def service_update(request, service_id):
    service = Services.objects.all()
    service_filter = ServicesFilter(request.GET, queryset=service)
    service_final = service_filter.qs

    particular_service = Services.objects.get(id=service_id)
    form = ServicesForm(instance=particular_service)
    if request.method == "POST":
        form = ServicesForm(request.POST, instance=particular_service)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Service has been updated.')
            return redirect('/a/service')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Failed to update service, please try again!!!')
            return render(request, 'admindashboard/servie.html', {'services': service_final, 'service_filter': service_filter, 'form': form, 'BTM': 'Update', 'service': 'selected'})
    dictionary = {'services': service_final, 'service_filter': service_filter,
                  'form': form, 'BTM': 'Update', 'service': 'selected'}
    return render(request, 'admindashboard/service.html', dictionary)


# <<====================Business====================>>
def business(request):
    business = Business.objects.all()
    business_filter = BusinessFilter(request.GET, queryset=business)
    business_final = business_filter.qs

    dictionary = {
        'businesses': business_final,
        'business_filter': business_filter,
        'business': 'selected'
    }
    return render(request, 'admindashboard/business.html', dictionary)


def business_verified(request, business_id):
    particular_business = Business.objects.get(id=business_id)
    particular_business.is_verified = True
    particular_business.save()
    return redirect("/a/business")

def business_not_verified(request, business_id):
    particular_business = Business.objects.get(id=business_id)
    particular_business.is_verified = False
    particular_business.save()
    return redirect("/a/business")

def business_view(request, business_id):
    particular_business = Business.objects.get(id=business_id)
    business_services = Business_Service.objects.filter(
        business=particular_business).all()
    business_gallery = Gallery.objects.filter(business=particular_business).all()
    business_workers = Worker.objects.filter(business=particular_business).all()
    business_hires = Hiring.objects.filter(
        business_service__business=particular_business)
    business_notifications = Notification.objects.filter(
        business=particular_business).all()
    business_reviews = Review.objects.filter(business=particular_business).all()
    business_bookmarks = Bookmark.objects.filter(business=particular_business).all()

    dictionary = {
        'pb': particular_business,
        'services': business_services,
        'services_count': business_services.count(),
        'gallery': business_gallery,
        'gallery_count': business_gallery.count(),
        'workers': business_workers,
        'workers_count': business_workers.count(),
        'hires': business_hires,
        'hires_count': business_hires.count(),
        'notifications': business_notifications,
        'notifications_count': business_notifications.count(),
        'reviews': business_reviews,
        'reviews_count': business_reviews.count(),
        'bookmarks': business_bookmarks,
        'bookmarks_count': business_bookmarks.count(),
        'business': 'selected'
    }
    return render(request, 'admindashboard/business_view.html', dictionary)

# <<====================Customer====================>>


def customer(request):
    customer = Customer.objects.all()
    customer_filter = CustomerFilter(request.GET, queryset=customer)
    customer_final = customer_filter.qs

    dictionary = {'customers': customer_final,
                  'customer_filter': customer_filter, 'customer': 'selected'}
    return render(request, 'admindashboard/customer.html', dictionary)


def customer_view(request, customer_id):
    particular_customer = Customer.objects.get(id=customer_id)

    customer_hires = Hiring.objects.filter(customer=particular_customer)
    customer_notifications = Notification.objects.filter(
        customer=particular_customer).all()
    customer_reviews = Review.objects.filter(customer=particular_customer).all()
    customer_bookmarks = Bookmark.objects.filter(customer=particular_customer).all()

    dictionary = {
        'pc': particular_customer,
        'hires': customer_hires,
        'hires_count': customer_hires.count(),
        'notifications': customer_notifications,
        'notifications_count': customer_notifications.count(),
        'reviews': customer_reviews,
        'reviews_count': customer_reviews.count(),
        'bookmarks': customer_bookmarks,
        'bookmarks_count': customer_bookmarks.count(),
        'customer': 'selected'
    }
    return render(request, 'admindashboard/customer_view.html', dictionary)


# <<====================Activities====================>>
def activities(request):
    dictionary = {'activities': 'selected'}
    return render(request, 'admindashboard/activities.html', dictionary)
