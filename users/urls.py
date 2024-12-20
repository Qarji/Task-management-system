from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),  # URL для отображения шаблона
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]