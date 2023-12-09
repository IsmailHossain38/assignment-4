from django import forms
from .models import Taskmodel

class Taskform(forms.ModelForm):
    class Meta:
        model = Taskmodel
        fields="__all__"