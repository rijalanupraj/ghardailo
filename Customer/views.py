# from django.shortcuts import render

# from .forms import CustomerRegistrationForm, CustomerProfileForm
# from django.contrib import messages

# # Create your views here.

# class CustomerRegistrationView(View):
#     def get(self, request):
#         form = CustomerRegistrationForm()
#         return render(request, 'app/customerregistration.html',{'form':form})
#     def post(self, request):
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             messages.success(request, 'Congratulations!! Registered Succcessfully')
#             form.save()
#         return render(request, 'app/customerregistration.html',{'form':form})