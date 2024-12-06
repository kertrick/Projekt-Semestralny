// Отримуємо посилання на елементи HTML
const taskInput = document.getElementById("taskInput");
const addButton = document.getElementById("addButton");
const taskList = document.getElementById("taskList");

// Функція для відображення завдань зі збережених даних
function loadTasks() {
    // Отримуємо завдання з LocalStorage
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];

    // Додаємо кожне завдання до списку
    tasks.forEach((task) => {
        createTaskElement(task);
    });
}

// Функція для створення нового елемента завдання
function createTaskElement(taskText) {
    const li = document.createElement("li");// зхвлалпзхвлапзщпькзрпщпкрзщклрезк

    const span = document.createElement("span");
    span.textContent = taskText;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Видалити";
    deleteButton.classList.add("delete-button");

    // Додаємо подію для видалення завдання
    deleteButton.addEventListener("click", () => {
        li.remove();
        saveTasks(); // Оновлюємо LocalStorage після видалення
    });

    li.appendChild(span);
    li.appendChild(deleteButton);
    taskList.appendChild(li);
}

// Функція для збереження завдань у LocalStorage
function saveTasks() {
    const tasks = [];
    taskList.querySelectorAll("li span").forEach((span) => {
        tasks.push(span.textContent);
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Подія для кнопки додавання завдання
addButton.addEventListener("click", () => {
    const taskText = taskInput.value.trim();
    if (taskText !== "") {
        createTaskElement(taskText);
        saveTasks(); // Зберігаємо завдання після додавання
        taskInput.value = ""; // Очищаємо поле вводу
    }
});

// Завантажуємо завдання при завантаженні сторінки
document.addEventListener("DOMContentLoaded", loadTasks);