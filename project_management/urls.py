from django.contrib import admin
from django.urls import path, include
from .views import main_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Пример: маршруты из приложения users
    path('tasks/', include('tasks.urls')), # Пример: маршруты из приложения tasks
]
