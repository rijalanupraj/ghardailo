# External Import
from django.urls import path

# Internal Import
from . import views

urlpatterns = [
    path('activate/<uidb64>/<token>/',
         views.activate_account, name='email-activate'),
]
