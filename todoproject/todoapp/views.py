from django.http import HttpResponse
from django.shortcuts import render, redirect

from todoapp.forms import ToDo_Form
from todoapp.models import Task


# Create your views here.
def todo(request):
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    task1 = Task.objects.all()
    return render(request, 'home.html', {'task1': task1})


def detail(request):
    task1 = Task.objects.all
    return render(request, 'detail.html', {'task1': task1})


from django.shortcuts import get_object_or_404


def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})


#
def update(request, id):
    task = Task.objects.get(id=id)
    f = ToDo_Form(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'f': f})
