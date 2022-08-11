from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
# Tuple for feedback type choices
FEEDBACK_TYPE_CHOICES = (
    ('G', 'I like it!'),
    ('NT', 'Everything need to be improved'),
    ('CSS', 'Need style improvement'),
    ('FT', 'Need features improvement'),
)
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name