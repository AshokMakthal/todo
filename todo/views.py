from django.shortcuts import redirect, render
from django.http import HttpResponse
from todo.models import Task
from django.shortcuts import get_object_or_404
# Create your views here.

def addTask(request):
   task = request.POST['task']
   Task.objects.create(task=task)
   return redirect('home')

def mark_as_done(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    task.is_completed=True
    task.save()
    return redirect('home')
def mark_as_undone(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context={
            "task": task
        }
        
        return render(request, "edit_task.html", context)
    
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')