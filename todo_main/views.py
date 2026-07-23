from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('created_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('created_at')

    return render(request, "home.html", {"tasks": tasks, "completed_tasks": completed_tasks})