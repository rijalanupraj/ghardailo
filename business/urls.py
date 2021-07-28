# External Import
from django.urls import path
from .import views
# Internal Import


urlpatterns = [
    path('business-profile/<str:slug>/',
         views.BusinessProfileView.as_view(), name='business-profile')

]
