from django.shortcuts import render
from django.http import request
from rest_framework import viewsets,status
from .models import *
from .forms import TaskForm
from .serializers import *
from rest_framework.response import Response

class taskViewSet(viewsets.ViewSet):
    def createTask(self,request):
        if request.method=='POST':
            form=TaskForm(request.POST)
            serialized=TaskSerializer(data=form)
            if serialized.is_valid():
                serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        else:
            form=TaskForm()
        return render(request,'templates/taskForm.html',{'form':form})

    def listTasks(self, request):
        queryset = task.objects.all()
        serialized= TaskSerializer(queryset,many=True)
        return Response(serialized.data)
    
    #def updateTask(self,request,pk=None):
        #task=task.object.get(pk=pk)

#class CalcViewSet(viewsets.ViewSet):
    #queryset = calc.objects.all()
    #serializer_class = CalcSerializer