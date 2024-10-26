from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TaskCreateApiView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
