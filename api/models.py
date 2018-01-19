from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone
from django.urls import reverse

from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    finish = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('index')
    def __str__(self):
        return self.title
