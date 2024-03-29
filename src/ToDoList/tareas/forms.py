from django.forms import ModelForm

from .models import Task


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'expiration_day','user']


class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'expiration_day', 'coment', 'status']