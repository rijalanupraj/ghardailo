from django.shortcuts import render

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
        'notification': notification
    }
    return render(request, 'admindashboard/dashboard.html', dictionary)