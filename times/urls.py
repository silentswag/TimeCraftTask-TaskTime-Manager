from . import views
from django.urls import path
from .models import *
from .views import *

urlpatterns= [path('create/',tasklc.as_view()),
              path('list/', level.as_view()),
              path('list/<str:level>/', level.as_view()),
              path('today/',today.as_view())
             ]