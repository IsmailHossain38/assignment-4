from django.db import models
from TaskCategory.models import Taskcategory
# Create your models here.

class Taskmodel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date = models.DateField(auto_now_add=True)
    add_cat = models.ManyToManyField(Taskcategory)
    def __str__(self) :
        return self.taskTitle
    
