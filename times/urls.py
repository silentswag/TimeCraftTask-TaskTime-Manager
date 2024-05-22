from . import views
from django.urls import path
from .models import *

urlpatterns= [path('task/', views.taskViewSet.as_view({'post':'createTask','get':'listTasks'}),name='create-list')]