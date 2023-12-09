from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        catform = forms.CategoryForm(request.POST)
        if catform.is_valid():
            catform.save()
            return redirect("add_category")   
    else:
        catform = forms.CategoryForm()
    
    return render(request,'first/add_category.html' ,{"data": catform})