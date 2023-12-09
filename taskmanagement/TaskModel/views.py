from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        taskform = forms.Taskform(request.POST)
        if taskform.is_valid():
            taskform.save()
            return redirect("add_task")   
    else:
        taskform = forms.Taskform()
         
    return render(request,'second/add_task.html' ,{"form": taskform})


def edit_task(request,id):
    taskModel = models.Taskmodel.objects.get(pk=id)
    Model = forms.Taskform(instance=taskModel)
    if request.method == 'POST':
        taskform = forms.Taskform(request.POST , instance=taskModel)
        if taskform.is_valid():
            taskform.save()
            return redirect("homepage")   

    return render(request,'second/add_task.html' ,{"form": Model})


def delete_task(request,id):
    taskModel = models.Taskmodel.objects.get(pk=id)
    taskModel.delete()
    return redirect("homepage")