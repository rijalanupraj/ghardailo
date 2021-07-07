# External Import
from django.urls import path
from .import views

# Internal Import
from .views import(
    BusinessListPageView
)


urlpatterns = [
    path('business/', BusinessListPageView.as_view(), name='business-list-page'),
    path('business-profile/<str:slug>/',
         views.BusinessProfileView.as_view(), name='business-profile')
]
