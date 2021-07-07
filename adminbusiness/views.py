from django.shortcuts import render

# Create your views here.
def businessDashboard(request):
    return render(request, 'adminbusiness/base/dashboard.html')

def editProfile(request):
    return render(request, 'adminbusiness/base/edit-profile.html')