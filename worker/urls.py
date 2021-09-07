from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.workerDashboard, name="worker-dashboard"),
    path('workerProfile/<int:worker_id>',
         views.getProfile, name="worker-profile"),
    path('hiring', views.WorkerHiringListView.as_view(), name="worker-hiring-list"),
    path('hirings/complete/<int:id>', views.complete_worker_hiring,
         name='complete-worker-hiring'),
    path('changePassword', views.change_password, name='change-password'),
    path('editProfile', views.editWorker, name='edit-profile'),
]

app_name = 'worker'
