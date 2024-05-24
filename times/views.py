from django.shortcuts import render,redirect
from django.http import request
from django.urls import reverse
from rest_framework import generics,status
from .models import *
from .forms import TaskForm
from .serializers import *
from rest_framework.response import Response

class taskViewSet(generics.GenericAPIView):
    queryset = task.objects.all()
    serialized= TaskSerializer(queryset,many=True)
    formClass= TaskForm
    template='taskForm.html'

    def get(self, request, *args, **kwargs):
        form = self.formClass()
        return render(request, self.template, {'form': form})

    def createTask(self,request, *args, **kwargs):
        form = self.formClass(request.POST)
        if form.is_valid():
            serializer = TaskSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                return redirect(reverse('task-form-view'))
            else:
                return render(request, self.template, {'form': form, 'errors': serializer.errors})
        else:
            return render(request, self.template, {'form': form, 'errors': form.errors}) 
       