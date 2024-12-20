from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.task_board, name='task_board'),
    path('create/', views.create_task, name='create_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
