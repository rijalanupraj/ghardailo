from django.shortcuts import render

# Internal Improt
from service.models import Services
from customer.models import Customer

# Create your views here.



def main_homepage(request):

    service = Services.objects.filter(is_active=True)[:6]
    context = {
        'services': service,
    }
    return render(request, 'homepage/home-page.html',context)


def about_us(request):


    return render(request, 'homepage/Aboutus.html')






