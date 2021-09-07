from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.workerDashboard, name="workerDashboard"),
    path('workerProfile/<int:worker_id>', views.getProfile, name="workerProfile"),
    path('hiring', views.WorkerHiringListView.as_view(), name="WorkerHiringdash"),
    path('hirings/complete/<int:id>', views.complete_worker_hiring,
        name='complete_worker_hiring'),
    path('changePassword', views.change_password, name='changePasswordDash'),
    path('editProfile', views.editWorker, name='editProfileDash'),
]
