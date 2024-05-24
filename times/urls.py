from . import views
from django.urls import path
from .models import *
from .views import *

urlpatterns= [path('task/',taskViewSet.as_view(),name='task=form-view')]