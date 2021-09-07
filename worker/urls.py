from django.urls import path, include
from . import views

urlpatterns = [
    path('workerProfile/<int:worker_id>', views.getProfile, name="workerProfile"),


]
