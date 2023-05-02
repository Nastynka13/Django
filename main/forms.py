from django.db.models import DateTimeField

from .models import Task, Reg
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            })
        }

class RegForm(ModelForm):
    class Meta:
        model = Reg
        fields = ["title", "setup", "time", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            "setup": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите прибор'
            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите время использования'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание задачи'
            }),
        }

