from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import (Garden, GardenMembership, Plant, Task, Comment, Activity)



# python manage.py test gardens

# Django runs setUp() before every test.
# So instead of manually recreating: User, Garden, Membership
# for every test, Django does it automatically.

# Conceptually:
# Test 1
#    ↓
# setUp()
#    ↓
# fresh database

# Test 2
#    ↓
# setUp()
#    ↓
# fresh database

# ...Other tests...


# This is much safer than testing against your real GardenOps database.









# Garden API Tests
class GardenAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="mom",
            password="testpassword"
        )

        self.garden = Garden.objects.create(
            name="Test Garden",
            description="Garden for API tests"
        )

        GardenMembership.objects.create(
            garden=self.garden,
            user=self.user,
            role="OWNER"
        )

    def test_get_garden(self):
        response = self.client.get(
            f"/api/gardens/{self.garden.id}/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["name"],
            "Test Garden"
        )

    def test_get_nonexistent_garden(self):
        response = self.client.get(
            "/api/gardens/99999/"
        )

        self.assertEqual(response.status_code, 404)

    def test_get_garden_list(self):
        response = self.client.get(
            "/api/gardens/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)









# Plant API Tests
class PlantAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="mom",
            password="testpassword"
        )

        self.garden = Garden.objects.create(
            name="Test Garden",
            description="Garden for API tests"
        )

        GardenMembership.objects.create(
            garden=self.garden,
            user=self.user,
            role="OWNER"
        )

        self.plant = Plant.objects.create(
            garden=self.garden,
            name="Tomato",
            description="Cherry tomato plant"
        )

    def test_get_plant(self):
        response = self.client.get(
            f"/api/plants/{self.plant.id}/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["name"],
            "Tomato"
        )
        self.assertEqual(
            response.data["garden"],
            self.garden.id
        )

    def test_get_plant_list(self):
        response = self.client.get(
            "/api/plants/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["name"],
            "Tomato"
        )

    def test_get_nonexistent_plant(self):
        response = self.client.get(
            "/api/plants/99999/"
        )

        self.assertEqual(response.status_code, 404)









class TaskAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="mom",
            password="testpassword"
        )

        self.garden = Garden.objects.create(
            name="Test Garden",
            description="Garden for API tests"
        )

        GardenMembership.objects.create(
            garden=self.garden,
            user=self.user,
            role="OWNER"
        )

        self.plant = Plant.objects.create(
            garden=self.garden,
            name="Tomato",
            description="Cherry tomato plant"
        )

        self.task = Task.objects.create(
            garden=self.garden,
            title="Water the tomatoes",
            description="Water every morning",
            assignee=self.user,
            status=Task.Status.TODO,
            plant=self.plant
        )

    def test_get_task(self):
        response = self.client.get(
            f"/api/tasks/{self.task.id}/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["title"],
            "Water the tomatoes"
        )
        self.assertEqual(
            response.data["garden"],
            self.garden.id
        )


    def test_get_task_list(self):
        response = self.client.get(
            "/api/tasks/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    # test POST
    def test_create_task(self):
        data = {
            # The JSON/API field name comes from your serializer, not directly from the Django database column naming.
            # so not "garden_id": self.garden.id
            "garden": self.garden.id,
            "title": "Water the basil",
            "description": "Water the basil plant",
            "assignee": self.user.id,
            "status": "TODO",
            "plant": self.plant.id
        }

        response = self.client.post(
            "/api/tasks/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data["title"],
            "Water the basil"
        )

        self.assertTrue(
            Task.objects.filter(
                title="Water the basil"
            ).exists()
        )

    # test PATCH
    def test_update_task(self):
        response = self.client.patch(
            f"/api/tasks/{self.task.id}/",
            {
                "status": "DONE"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["status"],
            "DONE"
        )

        # reloads the object from PostgreSQL
        self.task.refresh_from_db()

        self.assertEqual(
            self.task.status,
            Task.Status.DONE
        )

    # test task DELETE
    def test_delete_task(self):
        task_id = self.task.id

        response = self.client.delete(
            f"/api/tasks/{task_id}/"
        )

        self.assertEqual(response.status_code, 204)

        self.assertFalse(
            Task.objects.filter(id=task_id).exists()
        )


    def test_get_nonexistent_task(self):
        response = self.client.get(
            "/api/tasks/99999/"
        )

        self.assertEqual(response.status_code, 404)


# Error-case tests: test invalid input.
    def test_create_task_without_garden(self):
        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Invalid task"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

    def test_create_task_with_invalid_garden(self):
        response = self.client.post(
            "/api/tasks/",
            {
                "garden": 99999,
                "title": "Invalid garden task"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)


    def test_update_task_with_invalid_status(self):
        response = self.client.patch(
            f"/api/tasks/{self.task.id}/",
            {
                "status": "BANANA"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)

# Relationship tests
    def test_task_belongs_to_garden(self):
        self.assertEqual(
            self.task.garden,
            self.garden
        )

    def test_task_belongs_to_plant(self):
        self.assertEqual(
            self.task.plant,
            self.plant
        )

    def test_plant_has_tasks(self):
        self.assertIn(
            self.task,
            self.plant.tasks.all()
        )







class CommentAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="mom",
            password="testpassword"
        )

        self.garden = Garden.objects.create(
            name="Test Garden"
        )

        GardenMembership.objects.create(
            garden=self.garden,
            user=self.user,
            role="OWNER"
        )

        self.task = Task.objects.create(
            garden=self.garden,
            title="Water the tomatoes",
            assignee=self.user
        )


    def test_create_comment(self):
        response = self.client.post(
            f"/api/tasks/{self.task.id}/comments/",
            {
                "author": self.user.id,
                "content": "The tomatoes look healthy."
            },
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data["content"],
            "The tomatoes look healthy."
        )
        self.assertEqual(
            response.data["task"],
            self.task.id
        )


    def test_get_task_comments(self):
        Comment.objects.create(
            task=self.task,
            author=self.user,
            content="Looks good."
        )

        response = self.client.get(
            f"/api/tasks/{self.task.id}/comments/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["content"],
            "Looks good."
        )


    def test_get_comments_for_nonexistent_task(self):
        response = self.client.get(
            "/api/tasks/99999/comments/"
        )

        self.assertEqual(response.status_code, 404)


# relationship test
    def test_task_has_comments(self):
        comment = Comment.objects.create(
            task=self.task,
            author=self.user,
            content="Test comment"
        )

        self.assertIn(
            comment,
            self.task.comments.all()
        )









class ActivityAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="mom",
            password="testpassword"
        )

        self.garden = Garden.objects.create(
            name="Test Garden"
        )

        GardenMembership.objects.create(
            garden=self.garden,
            user=self.user,
            role="OWNER"
        )


    def test_get_activities(self):
        Activity.objects.create(
            garden=self.garden,
            user=self.user,
            action=Activity.Action.CREATED_GARDEN,
            description="Mom created the garden"
        )

        response = self.client.get(
            "/api/activities/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["description"],
            "Mom created the garden"
        )


    def test_get_garden_activities(self):
        Activity.objects.create(
            garden=self.garden,
            user=self.user,
            action=Activity.Action.CREATED_GARDEN,
            description="Mom created the garden"
        )

        response = self.client.get(
            f"/api/gardens/{self.garden.id}/activities/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


    # test Activity is read-only
    def test_cannot_create_activity(self):
        response = self.client.post(
            "/api/activities/",
            {
                "garden": self.garden.id,
                "user": self.user.id,
                "action": "CREATED_GARDEN",
                "description": "Fake activity"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            405
        )



# Django
#    ↓
# Django ORM
#    ↓
# PostgreSQL
#    ↓
# Django REST Framework
#    ↓
# REST APIs
#    ↓
# Relationships
#    ↓
# Validation
#    ↓
# HTTP error handling
#    ↓
# Role/membership architecture
#    ↓
# Automated tests