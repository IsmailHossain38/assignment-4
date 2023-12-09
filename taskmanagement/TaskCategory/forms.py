from django import forms 
from .models import Taskcategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Taskcategory
        fields = "__all__"
    