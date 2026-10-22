
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render


def home(request):
    return render(request, "tasks/index.html")

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer


class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ["patch", "options", "head"]
