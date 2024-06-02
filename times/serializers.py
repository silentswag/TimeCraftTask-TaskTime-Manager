from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['task_id','task_name','desc','duration','start']

"""class CalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = calc
        fields = '__all__'
"""