from django.urls import path
from . import views

urlpatterns = [
    path('boards/', views.boards_list, name='boards'),
    path('boards/<int:board_id>/', views.board_detail, name='board_detail'),  # Просмотр доски
    path('create/', views.create_board, name='create_board'),
]
