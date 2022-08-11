from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
# Tuple for feedback type choices
FEEDBACK_TYPE_CHOICES = (
    ('GO', 'I like it!'),
    ('NO', 'Everything need to be improved'),
    ('SI', 'Need style improvement'),
    ('FI', 'Need features improvement'),
)
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    feedback = models.CharField(max_length=2, choices=FEEDBACK_TYPE_CHOICES, default='GO')
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return f'{self.get_feedback_display()} on {self.created_at}- {self.message}'