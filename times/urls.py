from . import views
from django.urls import path
from .models import *
from .views import *

urlpatterns= [path('create/',tasklc.as_view())]