from django.db import models
from django.db.models import CASCADE
# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=166)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title



