from django.shortcuts import render

# Internal Improt
from .models import Services

# Create your views here.
def Service(request):
    service = Services.objects.filter(is_active=True)
    context = {
        'services': service,
        'active_service':'active'
    }
    return render(request, 'links/services.html', context)