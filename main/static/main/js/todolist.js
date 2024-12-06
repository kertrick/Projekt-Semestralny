document.addEventListener("DOMContentLoaded", function () {
    const taskInput = document.getElementById('taskInput');
    const addButton = document.getElementById('addButton');
    const taskList = document.getElementById('taskList');
  
    addButton.addEventListener('click', function (event) {
        event.preventDefault(); // Запобігаємо оновленню сторінки
  
        const taskText = taskInput.value.trim(); // Отримуємо введений текст
  
        if (taskText !== '') {
            const listItem = document.createElement('li'); // Створюємо новий елемент списку
            listItem.className = 'task-item'; // Додаємо клас для стилів
  
            const taskSpan = document.createElement('span'); // Створюємо контейнер для тексту задачі
            taskSpan.textContent = taskText; // Додаємо текст задачі
            listItem.appendChild(taskSpan); // Додаємо текст у елемент списку
  
            const deleteButton = document.createElement('button'); // Створюємо кнопку "Видалити"
            deleteButton.textContent = 'Видалити'; // Текст кнопки
            deleteButton.className = 'delete-button'; // Додаємо клас для стилів
            deleteButton.addEventListener('click', function () {
                taskList.removeChild(listItem); // Видаляємо елемент списку
            });
  
            listItem.appendChild(deleteButton); // Додаємо кнопку "Видалити" до елемента списку
            taskList.appendChild(listItem); // Додаємо елемент у список
  
            taskInput.value = ''; // Очищаємо поле вводу
        }
    });
  });
  
