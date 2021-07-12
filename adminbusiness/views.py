from business.models import Business
from django.shortcuts import render
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
    business = Business.objects.all()
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

def editProfile(request):
    return render(request, 'adminbusiness/base/edit-profile.html')