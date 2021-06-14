from django.db import models

# Create your models here.
class Services(models.Model):
    picture = models.ImageField(upload_to="static/uploads", null=True)
    name = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name