from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('my-admin-dashboard')
            elif request.user.is_business:
                return redirect('businessDash')
            elif request.user.is_customer:
                return redirect('home')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function


def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        elif request.user.is_business:
            return redirect('businessDash')
        else:
            return redirect('home')
    return wrapper_function


def business_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_business:
            return view_function(request, *args, **kwargs)        
        elif request.user.is_staff:
            return redirect('my-admin-dashboard')
        else:
            return redirect('home')
    return wrapper_function


def customer_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_customer:
            return view_function(request, *args, **kwargs)      
        if request.user.is_staff:
            return redirect('my-admin-dashboard')
        else:
            return redirect('businessDash')
    return wrapper_function
