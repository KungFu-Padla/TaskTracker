"""
TaskTracker — прототип системы управления личными задачами.
Лабораторная работа № 7 (прототип в IDE).
Страницы интерфейса — ЛР 6 (docs/lab6_figma/).
"""

from flask import Flask, jsonify, request, abort, send_from_directory

app = Flask(__name__)

# В памяти (для прототипа). В реальном проекте — база данных.
tasks = []
_next_id = 1


def _abort_if_not_found(task_id):
    if not any(t["id"] == task_id for t in tasks):
        abort(404, description=f"Задача с id={task_id} не найдена")


# ======================
# Страницы интерфейса (ЛР 6)
# ======================

@app.route("/")
def index():
    """Экран 1 — Вход / Регистрация."""
    return send_from_directory("docs/lab6_figma", "screen1_login.html")


@app.route("/list")
def task_list_page():
    """Экран 2 — Список задач."""
    return send_from_directory("docs/lab6_figma", "screen2_task_list.html")


@app.route("/new")
def new_task_page():
    """Экран 3 — Создание задачи."""
    return send_from_directory("docs/lab6_figma", "screen3_task_form.html")


@app.route("/task/<int:task_id>")
def task_card_page(task_id):
    """Экран 4 — Карточка задачи."""
    return send_from_directory("docs/lab6_figma", "screen4_task_card.html")


# ======================
# API
# ======================

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