from django.db import models
from hiring.models import *
from worker.models import *

class WCB(models.Model):
    hiring = models.ForeignKey(Hiring, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
