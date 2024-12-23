from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm


@login_required
def task_board(request):
    # Получаем задачи, созданные текущим пользователем
    boards = Board.objects.filter(user=request.user)
    return render(request, 'boards_menu.html', {'boards': boards})

def create_board(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        # Создаем доску, связывая ее с текущим пользователем
        Board.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            user=request.user  # Обязательно используйте текущего пользователя
        )
        return redirect('boards')

@login_required
def view_board(request, task_id):
    task = Board.objects.get(id=task_id, user=request.user)  # Убедитесь, что доска принадлежит пользователю
    return render(request, 'view_board.html', {'board': task})