from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail':'/task-detail/<str:pk>/',
        'Create':'/task-create',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    selializer = TaskSerializer(tasks, many=True)
    return Response(selializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    selializer = TaskSerializer(tasks, many=False)
    return Response(selializer.data)

@api_view(['POST'])
def taskCreate(request):
    selializer = TaskSerializer(data=request.data)

    if selializer.is_valid():
        selializer.save()

    return Response(selializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    selializer = TaskSerializer(instance=task, data=request.data)

    if selializer.is_valid():
        selializer.save()

    return Response(selializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item successfuly deleted")