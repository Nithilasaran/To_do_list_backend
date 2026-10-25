from app import app, create_table

create_table()

client = app.test_client()

# Add a task
response = client.post(
    "/tasks",
    json={"title": "Complete assignment"}
)
print("ADD TASK:", response.status_code)
print(response.get_json())

# View all tasks
response = client.get("/tasks")
print("\nVIEW TASKS:", response.status_code)
print(response.get_json())

# Delete the task we added
task_id = response.get_json()["tasks"][0]["id"]
response = client.delete(f"/tasks/{task_id}")
print("\nDELETE TASK:", response.status_code)
print(response.get_json())

# View tasks after deletion
response = client.get("/tasks")
print("\nTASKS AFTER DELETION:")
print(response.get_json())
