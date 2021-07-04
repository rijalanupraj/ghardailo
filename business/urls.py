# External Import
from django.urls import path

# Internal Import
from .views import(
    BusinessRegistartionCreateView,
    BusinessListPageView
)


urlpatterns = [
    path('register/', BusinessRegistartionCreateView.as_view(),
         name='business-registration'),
    path('business/', BusinessListPageView.as_view(), name='business-list-page')

]
