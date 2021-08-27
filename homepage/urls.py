from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_homepage, name='home'),
    path('aboutus', views.about_us, name='aboutus'),
]
