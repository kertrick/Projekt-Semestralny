from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from .views import todolist, update_task, delete_task, edit_task, CustomLoginView

urlpatterns = [
    # Перенаправление на страницу логина
    path('', lambda request: redirect('log', permanent=False)),

    # Ограниченные маршруты
    path('todolist/', login_required(views.todolist), name='todolist'),
    path('todolist/task/create/', login_required(views.todolist), name='task-create'),
    path('todolist/task/<int:task_id>/update/', login_required(views.update_task), name='task-update'),
    path('todolist/task/<int:task_id>/delete/', login_required(views.delete_task), name='task-delete'),
    path('todolist/task/<int:task_id>/edit/', login_required(views.edit_task), name='task-edit'),
    # Основные маршруты
    path('about', login_required(views.about), name='about'),
    path('todolist', login_required(views.todolist), name='todolist'),
    path('finance', login_required(views.finance), name='finance'),
    path('home', login_required(views.home), name='home'),
    path('acc', login_required(views.acc), name='acc'),

    # Регистрация и логин/логаут
    path('reg', views.user_register, name='reg'),  # Обработчик регистрации
    path('log', views.CustomLoginView.as_view(), name='log'),  # Используем CustomLoginView
    path('logout', LogoutView.as_view(next_page='log'), name='logout'),  # Логаут
]
