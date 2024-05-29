from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['id', 'task_name', 'desc', 'duration']
        exclude = ['start']  
        widgets = {
            'task_id': forms.Select(choices=task.TASK_ID_CHOICES),
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }