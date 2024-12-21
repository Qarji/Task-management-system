from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def task_board(request):
    # Получаем задачи, созданные текущим пользователем
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'boards_menu.html', {'tasks': tasks})

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
    return render(request, 'create_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if task:
        task.delete()
    return redirect('task_board')