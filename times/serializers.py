from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'

class CalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = calc
        fields = '__all__'
