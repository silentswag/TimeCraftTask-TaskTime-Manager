from django.db import models
from datetime import datetime
import uuid
from django.db import models
from datetime import datetime

class task(models.Model):
    TASK_ID_CHOICES = [
        ('Top', 'top'),
        ('Low', 'low'),
        ('Mid', 'mid'),
        # Add more choices as needed
    ]
    
    task_id = models.CharField(max_length=20, choices=TASK_ID_CHOICES,default='mid')
    task_name = models.CharField(max_length=50,unique=True)  # task_name should still be unique if required
    desc = models.TextField(max_length=200)
    duration = models.DurationField()
    start = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

       
    
"""class calc(models.Model):
    taskName=models.ForeignKey(to=task,on_delete=models.CASCADE)
    numsTask=models.IntegerField()
    weekly=models.FloatField()

    def __str__(self):
        return f'calcultions for {self.task.taskName}' """