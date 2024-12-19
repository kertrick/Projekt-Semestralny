from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def todolist(request):
    # Обробка форми додавання задачі
    if request.method == 'POST' and 'text' in request.POST:
        Task.objects.create(text=request.POST['text'])
        return redirect('todolist')

    # Отримання всіх задач (для всіх користувачів)
    tasks = Task.objects.all()
    return render(request, 'main/todolist.html', {'tasks': tasks})

def update_task(request, task_id):
    # Оновлення статусу виконання задачі
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.is_completed = 'is_completed' in request.POST
        task.save()
        return redirect('todolist')

def delete_task(request, task_id):
    # Видалення задачі
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('todolist')

# Функции для рендеринга статичных страниц
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

# def todolist(request):
#     return render(request, 'main/todolist.html')

def finance(request):
    return render(request, 'main/finance.html')

def reg(request):
    return render(request, 'main/reg.html')

def log(request):
    return render(request, 'main/log.html')

def acc(request):
    return render(request, 'main/acc.html')

# Функция для регистрации пользователя
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log')  # Перенаправляем на страницу логина
    else:
        form = UserCreationForm()
    return render(request, 'main/reg.html', {'form': form})

# Функция для логина пользователя
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acc')  # Перенаправляем на страницу аккаунта
        else:
            return HttpResponse('Неправильный логин или пароль')
    return render(request, 'main/log.html')

# Функция для логаута пользователя
def user_logout(request):
    logout(request)
    return redirect('home')




       
