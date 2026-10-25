
# To-Do List Backend

## Aim
To develop a backend application for adding, viewing, and deleting tasks.

## Technologies Used
- Python
- Flask
- SQLite
- REST API

## Features
- Add a task
- View all tasks
- Delete a task
- Store tasks in an SQLite database
- Validate task titles

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Check API status |
| POST | /tasks | Add a task |
| GET | /tasks | View all tasks |
| DELETE | /tasks/<id> | Delete a task |

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open http://127.0.0.1:5000/ in your browser.

## Run Tests

```bash
python test_api.py
```

## Result
The To-Do List backend provides APIs to add, view, and delete tasks using Flask and SQLite.
