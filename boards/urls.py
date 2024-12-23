from django.urls import path
from . import views

urlpatterns = [
    path('boards/', views.task_board, name='boards'),
    path('boards/<int:board_id>/', views.view_board, name='view_board'),  # Просмотр доски
    path('create/', views.create_board, name='create_board'),
]
