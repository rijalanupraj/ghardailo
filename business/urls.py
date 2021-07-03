# External Import
from django.urls import path

# Internal Import
from .views import(
    BusinessRegistartionCreateView,
    BusinessLoginView
)


urlpatterns = [
    path('register/', BusinessRegistartionCreateView.as_view(),
         name='business-registration'),
    path('login/', BusinessLoginView.as_view(), name="business-login"),
]
