from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.all().values
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)

def add_task(request):
    return render(request, 'add_task.html')
