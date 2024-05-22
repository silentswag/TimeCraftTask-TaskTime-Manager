from django.shortcuts import render
from django.http import request
from rest_framework import viewsets,status
from .models import *
from .serializers import *
from rest_framework.response import Response

class taskViewSet(viewsets.ViewSet):
    def createTask(self,request):
        serialized=TaskSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def listTasks(self, request):
        queryset = task.objects.all()
        serialized= TaskSerializer(queryset,many=True)
        return Response(serialized.data)
    
    #def updateTask(self,request,pk=None):
        #task=task.object.get(pk=pk)

#class CalcViewSet(viewsets.ViewSet):
    #queryset = calc.objects.all()
    #serializer_class = CalcSerializer