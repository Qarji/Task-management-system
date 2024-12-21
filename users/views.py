from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Главная страница (пример)
def main_menu(request):
    return render(request, 'main_menu.html')  # Убедитесь, что путь к шаблону корректный

# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Авторизация
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_menu')  # Перенаправляем на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Выход из системы
def logout_view(request):
    logout(request)
    return redirect('main_menu')  # Перенаправляем на главную страницу