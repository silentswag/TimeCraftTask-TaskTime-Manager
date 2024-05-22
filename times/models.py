from django.db import models
from datetime import datetime
import uuid
class task(models.Model):
    id= models.CharField(primary_key=True,max_length=20)
    taskName=models.CharField(max_length=50)
    desc=models.TextField(max_length=200)
    duration=models.DurationField()
    start=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.taskName    
    
class calc(models.Model):
    taskName=models.ForeignKey(to=task,on_delete=models.CASCADE)
    today=models.IntegerField()
    weekly=models.FloatField()

    def __str__(self):
        return f'calcultions for {self.task.taskName}'