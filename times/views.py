from django.shortcuts import render,redirect
from django.http import request
from django.urls import reverse
from rest_framework import generics,status
from .models import *
from .forms import TaskForm
from .serializers import *
from rest_framework.response import Response

class tasklc(generics.ListCreateAPIView):
    queryset = task.objects.all()
    serializer_class= TaskSerializer
    formClass= TaskForm
    template='taskForm.html'
 
   