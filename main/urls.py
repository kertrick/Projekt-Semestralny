from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView

from .views import todolist, update_task, delete_task, edit_task

urlpatterns = [
    # Перенаправление на страницу логина
    path('', lambda request: redirect('log', permanent=False)),

    path('todolist/', todolist, name='todolist'),
    path('todolist/task/create/', todolist, name='task-create'),
    path('todolist/task/<int:task_id>/update/', update_task, name='task-update'),
    path('todolist/task/<int:task_id>/delete/', delete_task, name='task-delete'),
    path('todolist/task/<int:task_id>/edit/', edit_task, name='task-edit'),

    # Основные маршруты
    path('about', views.about, name='about'),
    path('todolist', views.todolist, name='todolist'),
    path('finance', views.finance, name='finance'),
    path('home', views.home, name='home'),
    path('acc', views.acc, name='acc'),

    # Регистрация и логин/логаут
    path('reg', views.user_register, name='reg'),  # Обработчик регистрации
    path('log', LoginView.as_view(template_name='main/log.html'), name='log'),  # Класс LoginView
    path('logout', LogoutView.as_view(next_page='log'), name='logout'),  # Логаут
]


