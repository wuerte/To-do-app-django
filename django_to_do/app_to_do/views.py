from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Task


def index(request):
    tasks = Task.objects.all().values
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


def add_task(request):
    return render(request, 'add_task.html')


def add_task_record(request):
    title_form = request.POST['title']
    description_form = request.POST['description']

    new_task = Task(title=title_form, description=description_form)
    new_task.save()

    return HttpResponseRedirect(reverse('index'))
