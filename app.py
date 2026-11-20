"""
TaskTracker — прототип системы управления личными задачами.
Лабораторная работа № 7 (прототип в IDE).
"""

from flask import Flask, jsonify, request, abort, Response

app = Flask(__name__)

# В памяти (для прототипа). В реальном проекте — база данных.
tasks = []
_next_id = 1


def _abort_if_not_found(task_id):
    if not any(t["id"] == task_id for t in tasks):
        abort(404, description=f"Задача с id={task_id} не найдена")


@app.route("/")
def index():
    """Корневая страница — простой интерфейс прототипа."""
    return Response("""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TaskTracker</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Inter', 'Roboto', 'Segoe UI', sans-serif; background: #f3f4f6; color: #111827; min-height: 100vh; }
  .navbar { background: #fff; border-bottom: 1px solid #e5e7eb; padding: 12px 16px; display: flex; justify-content: space-between; align-items: center; }
  .navbar h1 { font-size: 18px; font-weight: 600; }
  .badge { background: #dcfce7; color: #166534; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 600; }
  .container { max-width: 700px; margin: 24px auto; padding: 0 16px; }
  .card { background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 24px; margin-bottom: 16px; }
  h2 { font-size: 20px; margin-bottom: 16px; }
  .form-group { margin-bottom: 12px; }
  label { display: block; margin-bottom: 6px; font-size: 14px; color: #374151; }
  input { width: 100%; padding: 10px 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 14px; }
  input:focus { outline: none; border-color: #3b82f6; }
  .btn { padding: 10px 16px; border: none; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; }
  .btn-primary { background: #3b82f6; color: #fff; }
  .btn-primary:hover { background: #2563eb; }
  .btn-done { background: #10b981; color: #fff; }
  .btn-done:hover { background: #059669; }
  .btn-delete { background: #fef2f2; color: #ef4444; }
  .btn-delete:hover { background: #fee2e2; }
  .task-list { list-style: none; }
  .task-item { display: flex; align-items: center; gap: 12px; padding: 12px; border-bottom: 1px solid #f3f4f6; }
  .task-item.done .title { text-decoration: line-through; color: #9ca3af; }
  .title { flex: 1; font-size: 15px; }
  .empty { text-align: center; padding: 32px; color: #6b7280; }
  .api-hint { font-size: 13px; color: #6b7280; margin-top: 12px; }
  code { background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 12px; }
</style>
</head>
<body>
  <nav class="navbar">
    <h1>TaskTracker — прототип</h1>
    <span class="badge">API работает</span>
  </nav>
  <div class="container">
    <div class="card">
      <h2>Добавить задачу</h2>
      <form id="create-form">
        <div class="form-group">
          <label>Название задачи</label>
          <input type="text" id="task-title" placeholder="Например: Купить хлеб" required>
        </div>
        <button type="submit" class="btn btn-primary">+ Создать</button>
      </form>
    </div>
    <div class="card">
      <h2>Список задач</h2>
      <ul class="task-list" id="task-list">
        <li class="empty">Загрузка...</li>
      </ul>
      <div class="api-hint">
        API: <code>GET /tasks</code> <code>POST /tasks</code> <code>POST /tasks/&lt;id&gt;/complete</code> <code>DELETE /tasks/&lt;id&gt;</code> <code>GET /health</code>
      </div>
    </div>
  </div>
  <script>
    async function loadTasks() {
      const resp = await fetch('/tasks');
      const tasks = await resp.json();
      const list = document.getElementById('task-list');
      if (!tasks.length) {
        list.innerHTML = '<li class="empty">Задач пока нет. Создайте первую!</li>';
        return;
      }
      list.innerHTML = tasks.map(t => `
        <li class="task-item ${t.done ? 'done' : ''}">
          <span class="title">${t.title}</span>
          ${t.done ? '' : `<button class="btn btn-done" onclick="completeTask(${t.id})">✓ Выполнить</button>`}
          <button class="btn btn-delete" onclick="deleteTask(${t.id})">Удалить</button>
        </li>
      `).join('');
    }
    async function createTask(title) {
      await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
      });
      loadTasks();
    }
    async function completeTask(id) {
      await fetch(`/tasks/${id}/complete`, { method: 'POST' });
      loadTasks();
    }
    async function deleteTask(id) {
      await fetch(`/tasks/${id}`, { method: 'DELETE' });
      loadTasks();
    }
    document.getElementById('create-form').addEventListener('submit', (e) => {
      e.preventDefault();
      const input = document.getElementById('task-title');
      if (input.value.trim()) {
        createTask(input.value.trim());
        input.value = '';
      }
    });
    loadTasks();
  </script>
</body>
</html>""", mimetype="text/html")


@app.route("/tasks", methods=["GET"])
def list_tasks():
    """Вернуть все задачи."""
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    """Создать новую задачу.
    Ожидается JSON: {"title": "..."}
    """
    global _next_id
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        abort(400, description="Поле title обязательно")
    task = {"id": _next_id, "title": title, "done": False}
    _next_id += 1
    tasks.append(task)
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    """Пометить задачу выполненной."""
    _abort_if_not_found(task_id)
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return jsonify(t)
    abort(404)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Удалить задачу."""
    _abort_if_not_found(task_id)
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"result": True})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)