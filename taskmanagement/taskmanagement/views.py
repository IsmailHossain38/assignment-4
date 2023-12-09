from django.shortcuts import render
from TaskModel.models import Taskmodel
def home(request):
    data = Taskmodel.objects.all()
    return render(request, 'home.html' ,{"Data":data})