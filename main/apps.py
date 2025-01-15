from django.apps import AppConfig
 
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Список для збереження завдань у пам'яті
tasks = []

@app.route('/')
def index():
    return render_template('todolist.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.json.get('taskText')
    if task_text:
        tasks.append(task_text)
        return jsonify({'status': 'success', 'taskText': task_text}), 200
    return jsonify({'status': 'error', 'message': 'Task text is required'}), 400

@app.route('/edit_task', methods=['POST'])
def edit_task():
    old_text = request.json.get('oldText')
    new_text = request.json.get('newText')

    if old_text and new_text:
        for i, task in enumerate(tasks):
            if task == old_text:
                tasks[i] = new_text
                return jsonify({'status': 'success', 'newText': new_text}), 200
        return jsonify({'status': 'error', 'message': 'Task not found'}), 404

    return jsonify({'status': 'error', 'message': 'Old and new text are required'}), 400

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_text = request.json.get('taskText')
    if task_text in tasks:
        tasks.remove(task_text)
        return jsonify({'status': 'success', 'taskText': task_text}), 200
    return jsonify({'status': 'error', 'message': 'Task not found'}), 404

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}), 200

if __name__ == '__main__':
    app.run(debug=True)


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
