from django.shortcuts import render,redirect
from django.http import request
from django.urls import reverse
from django.utils.timezone import localdate
from rest_framework import generics,status
from .models import *
from datetime import date
#from .forms import TaskForm
from .serializers import *
from rest_framework.response import Response

class tasklc(generics.CreateAPIView):
    queryset = task.objects.all()
    serializer_class= TaskSerializer
    #formClass= TaskForm
    #template='taskForm.html' 

class level(generics.ListAPIView):
    #queryset=task.objects.all()
    serializer_class= TaskSerializer

    def get_queryset(self):
        task_level=self.kwargs.get('level')
        if task_level:
            return task.objects.filter(task_id__icontains=task_level)
        else:
            return task.objects.all()

class today(generics.ListAPIView):
    serializer_class= TaskSerializer
    def get_queryset(self):
        today=localdate()
        queryset=task.objects.filter(start__date=today)
        return queryset
    