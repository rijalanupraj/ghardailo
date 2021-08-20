from django.shortcuts import render

# Internal Improt
from service.models import Services

# Create your views here.


def Home(request):

    service = Services.objects.filter(is_active=True)[:8]
    context = {
        'services': service,
    }
    return render(request, 'homepage/index.html', context)






