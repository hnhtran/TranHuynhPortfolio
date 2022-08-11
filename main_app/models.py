from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name