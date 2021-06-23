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
    business = User.Business.objects.all().count()
    gallery = Gallery.objects.all().count()
    worker = Worker.objects.all().count()
    customer = User.Customer.objects.all().count()
    service = Services.objects.all().count()
    hiring = hiring.objects.all().count()
    review = review.objects.all().count()
    notification = notification.objects.all().count()

    dictionary = {
        'user': user,
        'business': business,
        'gallery': gallery,
        'worker': worker,
        'customer': customer,
        'service': service,
        'hiring': hiring,
        'review': review,
        'notification': notification
    }
    return render(request, 'admindashboard/dashboard.html', dictionary)