# External Import
from django.urls import path

# Internal Import
from .views import(
    BusinessListPageView
)


urlpatterns = [
    path('business/', BusinessListPageView.as_view(), name='business-list-page')
]
