
# Extrenal Import
from business.models import Business_Profile
from django.shortcuts import render
# Internal Import

def BusinessProfile(request):
    profile = Business_Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'business/business-profile.html', context)

