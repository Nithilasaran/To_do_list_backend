from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "tasks.db"
)


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_db()
    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)
        connection.commit()
    finally:
        connection.close()


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "To-Do List API is running",
        "endpoints": [
            "POST /tasks",
            "GET /tasks",
            "DELETE /tasks/<id>"
        ]
    })


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send valid JSON data"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Task title is required"}), 400

    title = title.strip()

    if len(title) > 200:
        return jsonify({"error": "Task title is too long"}), 400

    connection = get_db()
    try:
        cursor = connection.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,)
        )
        connection.commit()

        return jsonify({
            "message": "Task added successfully",
            "task": {
                "id": cursor.lastrowid,
                "title": title,
                "completed": False
            }
        }), 201
    finally:
        connection.close()


@app.route("/tasks", methods=["GET"])
def get_tasks():
    connection = get_db()
    try:
        rows = connection.execute(
            "SELECT id, title, completed FROM tasks ORDER BY id"
        ).fetchall()

        tasks = [
            {
                "id": row["id"],
                "title": row["title"],
                "completed": bool(row["completed"])
            }
            for row in rows
        ]

        return jsonify({"tasks": tasks}), 200
    finally:
        connection.close()


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    connection = get_db()
    try:
        cursor = connection.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Task not found"}), 404

        return jsonify({
            "message": "Task deleted successfully",
            "id": task_id
        }), 200
    finally:
        connection.close()


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
