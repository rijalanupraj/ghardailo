from django.db import models
from hiring.models import *
from worker.models import *

class WCB(models.Model):
    hiring = models.OneToOneField(Hiring, on_delete=models.CASCADE)
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
