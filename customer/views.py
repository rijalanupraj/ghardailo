# External Import
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.db import transaction
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Internal Import

from django import forms
from .forms import CustomerUpdateForm
from django.contrib.auth import get_user_model
from .models import Customer

User = get_user_model()



#@login_required(login_url='/')

def profileupdate(request):
      cu_form = CustomerUpdateForm
      if request.method== 'POST':

         cu_form = CustomerUpdateForm(request.POST,request.FILES,instance=request.user.customer)

         if cu_form.is_valid():
              cu_form.save()
              messages.success(request, f' Your Account Has Been Successfully Updated')
              return redirect('customerprofile')

      else:
          
          cu_form= CustomerUpdateForm(instance=request.user.customer)

      context= {
            'cu_form': cu_form
      }
      

      return render(request, 'customer/customerprofile.html', context)




