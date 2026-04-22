from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    # Toggle status
    task.status = 'completed' if task.status == 'pending' else 'pending'
    task.save()

    return Response(TaskSerializer(task).data)


@api_view(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    task.delete()
    return Response({"message": "Task deleted"}, status=204)