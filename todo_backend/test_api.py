
import unittest
from app import app, create_table, get_db


class TodoAPITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_table()

    def setUp(self):
        self.client = app.test_client()

        # Keep test results repeatable by clearing old tasks.
        connection = get_db()
        connection.execute("DELETE FROM tasks")
        connection.commit()
        connection.close()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["message"],
            "To-Do List API is running"
        )

    def test_add_task(self):
        response = self.client.post(
            "/tasks",
            json={"title": "Complete assignment"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.get_json()["task"]["title"],
            "Complete assignment"
        )

    def test_view_tasks(self):
        self.client.post(
            "/tasks",
            json={"title": "Study Python"}
        )

        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()["tasks"]), 1)
        self.assertEqual(
            response.get_json()["tasks"][0]["title"],
            "Study Python"
        )

    def test_delete_task(self):
        response = self.client.post(
            "/tasks",
            json={"title": "Delete this task"}
        )
        task_id = response.get_json()["task"]["id"]

        delete_response = self.client.delete(
            f"/tasks/{task_id}"
        )
        self.assertEqual(delete_response.status_code, 200)

        list_response = self.client.get("/tasks")
        self.assertEqual(
            len(list_response.get_json()["tasks"]),
            0
        )

    def test_missing_task(self):
        response = self.client.delete("/tasks/999999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
