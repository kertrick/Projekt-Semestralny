const toggleButton = document.getElementById('toggle-button');
const panel = document.getElementById('sliding-panel');
const addButtonPanel = document.getElementById('add-button-panel');
const amountInput = document.getElementById('amount-input');
const categoryInput = document.getElementById('category-input');
const records = document.getElementById('records');
const circleTotal = document.getElementById('circle-total');
const totalBalance = document.getElementById('total-balance');

let total = 0;
let transactions = [];

// Функция для загрузки данных из LocalStorage
function loadTransactions() {
    const savedTransactions = localStorage.getItem('transactions');
    if (savedTransactions) {
        transactions = JSON.parse(savedTransactions);
        transactions.forEach(({ amount, category, isExpense }) => {
            // Отображаем каждую транзакцию в интерфейсе
            const record = document.createElement('div');
            record.textContent = `${category}: ${isExpense ? '-' : '+'}${amount} PLN`;
            records.appendChild(record);

            // Обновляем общий баланс
            total += isExpense ? -amount : amount;
        });
        updateUI();
    }
}

// Функция для сохранения данных
function saveTransactions() {
    localStorage.setItem('transactions', JSON.stringify(transactions));
}

// Функция для обновления интерфейса
function updateUI() {
    circleTotal.textContent = `${total} PLN`;
    totalBalance.textContent = total;
}

// Открытие/закрытие панели
toggleButton.addEventListener('click', function () {
    panel.classList.toggle('hidden');
});


// Добавление новой транзакции
addButtonPanel.addEventListener('click', function () {
    const amount = parseFloat(amountInput.value);
    const category = categoryInput.value.trim();
    const isExpense = document.getElementById('expenses-tab').classList.contains('active');

    if (isNaN(amount) || amount <= 0 || category === '') {
        alert('Введіть коректні дані!');
        return;
    }

    // Создание и отображение записи транзакции
    const record = document.createElement('div');
    record.textContent = `${category}: ${isExpense ? '-' : '+'}${amount} PLN`;
    records.appendChild(record);

    // Обновление общего баланса
    total += isExpense ? -amount : amount;
    updateUI();

    // Сохранение транзакции в массив и LocalStorage
    transactions.push({ amount, category, isExpense });
    saveTransactions();

    // Очистка полей ввода
    amountInput.value = '';
    categoryInput.value = '';
});

// Переключение вкладок
document.getElementById('expenses-tab').addEventListener('click', function () {
    this.classList.add('active');
    document.getElementById('income-tab').classList.remove('active');
});

document.getElementById('income-tab').addEventListener('click', function () {
    this.classList.add('active');
    document.getElementById('expenses-tab').classList.remove('active');
});

// Загрузка данных из LocalStorage при запуске приложения
loadTransactions();
