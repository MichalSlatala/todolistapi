from django.forms import ModelForm

from . import models

#forms goes here

class TaskForm(ModelForm):
    class Meta:
        model = models.Todo
        fields = ('title','text','created_at')
