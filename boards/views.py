from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from django.contrib.auth.decorators import login_required

@login_required
def create_board(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        Board.objects.create(
            title=title,
            description=description,
            user_id=request.user
        )
        return redirect('boards')

@login_required
def boards_list(request):
    boards = request.user.boards.all() 
    return render(request, 'boards_list.html', {'boards': boards})

@login_required
def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id, user=request.user)
    return render(request, 'board_detail.html', {'board': board})
