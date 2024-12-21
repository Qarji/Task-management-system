from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),  # URL для отображения шаблона
    path('register/', views.register, name='register'),  # Регистрация
    path('login/', views.login_view, name='login'),  # Авторизация
    path('logout/', views.logout_view, name='logout'),  # Выход из системы
]