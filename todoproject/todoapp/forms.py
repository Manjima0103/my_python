from .models import Task
from django import forms


class ToDo_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
