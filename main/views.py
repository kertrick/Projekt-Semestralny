from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm  # Если создаёшь кастомную форму
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    # Обробка форми додавання задачі
    if request.method == 'POST' and 'text' in request.POST:
        Task.objects.create(text=request.POST['text'], user=request.user)  # Прив'язуємо завдання до поточного користувача
        return redirect('todolist')

    # Отримання всіх задач, прив'язаних до поточного користувача
    tasks = Task.objects.filter(user=request.user)

    # Перевірка, чи передано завдання для редагування
    task_to_edit = None
    if 'task_to_edit' in request.POST:
        task_to_edit = get_object_or_404(Task, id=request.POST['task_to_edit'])

    # Розрахунок прогресу виконаних завдань
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()

    return render(request, 'main/todolist.html', {
        'tasks': tasks,
        'task_to_edit': task_to_edit,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
    })

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Перевірка, чи належить завдання поточному користувачу

    if request.method == 'POST':
        # Оновлення тексту завдання
        if 'text' in request.POST:
            task.text = request.POST['text']

        # Оновлення статусу виконання (якщо передано)
        task.is_completed = 'is_completed' in request.POST

        task.save()
        return redirect('todolist')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Перевірка, чи належить завдання поточному користувачу
    if request.method == 'POST':
        task.delete()
        return redirect('todolist')

def edit_task(request, task_id):
    
    # Обробка форми редагування тексту
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.text = request.POST.get('text', task.text)
        task.save()
        return redirect('todolist')

    # Рендер сторінки зі списком завдань, але з активною формою редагування
    tasks = Task.objects.all()  # Якщо потрібно тільки для певного користувача, використовуйте Task.objects.filter(user=request.user)
    return render(request, 'main/todolist.html', {
        'tasks': tasks,
        'task_to_edit': task  # Передаємо завдання, яке редагується
    })


# Функции для рендеринга статичных страниц
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

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
        form = CustomUserCreationForm(request.POST)  # Используем кастомную форму
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически логиним после регистрации
            return redirect('home')  # Перенаправление на мейн страницу
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/reg.html', {'form': form})

# Функция для логина пользователя
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу
        else:
            context = {'error': 'Неправильный логін або пароль'}  # Сообщение об ошибке
            return render(request, 'main/log.html', context)
    return render(request, 'main/log.html')

# Логаут
def user_logout(request):
    logout(request)
    return redirect('home')


class CustomLoginView(LoginView):
    template_name = 'main/log.html'  # Шаблон для страницы логина

    def form_invalid(self, form):
        # Добавляем сообщение об ошибке в контекст
        return self.render_to_response(self.get_context_data(form=form, error="Неправильный логін або пароль"))




