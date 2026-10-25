# To-Do List Backend API

## Project Overview

The To-Do List Backend API is a RESTful application developed using Python, Flask, and SQLite. It allows users to add tasks, retrieve the task list, and delete tasks through HTTP requests.

The project demonstrates basic backend development, database operations, and API testing.

## Objectives

- Create and manage tasks through API endpoints.
- Store task details in an SQLite database.
- Retrieve task records in JSON format.
- Delete tasks by their unique IDs.
- Test API responses and HTTP status codes.

## Technology Stack

- **Language:** Python
- **Backend Framework:** Flask
- **Database:** SQLite
- **Data Format:** JSON
- **Testing:** Python test script
- **Development Environment:** Visual Studio Code

## Features

- Add a new task.
- View all tasks.
- Delete a task by ID.
- Assign a unique ID to each task.
- Track task completion status.
- Return success and error responses.

## Project Structure

```text
todo_backend/
├── app.py
├── test_api.py
├── demo_tasks.py
├── requirements.txt
└── README.md
```

*Keep only the filenames that actually exist in your final project folder.*

## Installation and Setup

### 1. Check Python

```bash
python --version
```

### 2. Install dependencies

If `requirements.txt` is available:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install Flask:

```bash
python -m pip install flask
```

### 3. Run the application

```bash
python app.py
```

Keep the server running while testing the API.

### 4. Run the tests

Open another VS Code terminal and run the test script:

```bash
python test_api.py
```

If you use the demonstration script, run:

```bash
python demo_tasks.py
```

## API Endpoints

| HTTP Method | Purpose |
|---|---|
| POST | Add a task |
| GET | Retrieve all tasks |
| DELETE | Delete a task by ID |

Refer to `app.py` for the exact endpoint paths and request fields.

## Example Task

```json
{
  "title": "Complete assignment",
  "completed": false
}
```

## Testing Results

The following operations were successfully demonstrated:

1. **Add Task:** Returned HTTP `201` with the message `Task added successfully`.
2. **View Tasks:** Returned HTTP `200` and displayed the stored task.
3. **Delete Task:** Returned HTTP `200` with the message `Task deleted successfully`.
4. **View After Deletion:** Returned an empty task list.

## Future Enhancements

- Update task details.
- Mark tasks as completed.
- Add due dates and priorities.
- Add user-specific task lists.
- Improve input validation and automated testing.

## Author

Developed as a Web Development Technologies Lab project.
