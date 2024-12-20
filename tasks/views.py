from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_board(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/board.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Привязываем задачу к текущему пользователю
            task.save()
            return redirect('task_board')  # Перенаправление на доску задач
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if task:
        task.delete()
    return redirect('task_board')