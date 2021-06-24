# External Import
from django.urls import path

# Internal Import
from .views import(
    BusinessRegistartionCreateView
)


urlpatterns = [
    path('register/', BusinessRegistartionCreateView.as_view(success_url="/"),
         name='business-registration'),
]
