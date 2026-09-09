from django.db import models
from django.contrib.auth.models import User

# Garden ↔ User is many to many.

# laura = User.objects.get(username="Laura")
# garden.members.add(laura)
# garden.members.all()
# laura.gardens.all()
class Garden(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(
        User,
        through="GardenMembership",
        related_name="gardens",
        blank=True
    )

    def __str__(self):
        return self.name

# create vertual environment
# python -m venv .venv

# enter to venv
# .\.venv\Scripts\Activate.ps1

# Django REST Framework(DRF)
# backend will expose REST APIs to React.
# pip install djangorestframework

# cd backend, then Create the Django project
# django-admin startproject config .

# Python model
#      ↓
# makemigrations
#      ↓
# Migration file
#      ↓
# migrate
#      ↓
# Database

# python manage.py makemigrations
# python manage.py migrate



# garden-management/
# │
# ├── .venv/
# │
# └── backend/
#     │
#     ├── manage.py
#     │
#     ├── config/
#     │   ├── settings.py
#     │   ├── urls.py
#     │   ├── asgi.py
#     │   └── wsgi.py
#     │
#     ├── gardens/
#     │   ├── admin.py
#     │   ├── apps.py
#     │   ├── models.py
#     │   ├── tests.py
#     │   └── views.py
#     │
#     └── db.sqlite3


# conceptually:
# Garden Management
#        │
#        ▼
#     Django
#        │
#        ├── config
#        │     └── project configuration
#        │
#        └── gardens
#              └── garden-related functionality


# Python interactive shell >>> can type Python directly here.
# python manage.py shell

# Give me all Garden objects in the database.
# Garden.objects.all()
# garden = Garden.objects.first()
# garden.name


# SQL INSERT
# garden2 = Garden.objects.create(
#     name="Balcony Garden",
#     description="A small garden for herbs and tomatoes."
# )
# garden2
# Garden.objects.all()

# Count
# Garden.objects.count()

# find 
# garden = Garden.objects.get(name="Backyard Garden")
# garden.description

# Filtering
# Garden.objects.filter(name="Backyard Garden")
# => get() returns one object, filter() returns a QuerySet


# Modify
# Without save(), you changed the Python object in memory, but you haven't necessarily persisted the change to the database.
# garden = Garden.objects.get(name="Backyard Garden")
# garden.description = "A family garden for vegetables, herbs, and flowers."
# garden.save()

# Delete
# garden2.delete()


## Five ORM

# CREATE
# Garden.objects.create(...)

# READ
# Garden.objects.all()
# Garden.objects.get(...)
# Garden.objects.filter(...)

# UPDATE
# garden.save()

# DELETE
# garden.delete()

# CRUD
# | Operation | Meaning       |
# | --------- | ------------- |
# | Create    | Create data   |
# | Read      | Retrieve data |
# | Update    | Change data   |
# | Delete    | Remove data   |


# inspect the SQL
# Garden.objects.filter(name="Backyard Garden").query

# SELECT ...
# FROM "gardens_garden"
# WHERE "gardens_garden"."name" = Backyard Garden

# Python
# Garden.objects.filter(...)
#         ↓
# Django ORM
#         ↓
# SQL
#         ↓
# Database

# Exit the Django shell
# exit()

# For this project, I'm using
# Django
# +
# ORM
# +
# PostgreSQL
# +
# Docker





# an intermediate model
class GardenMembership(models.Model):
    class Role(models.TextChoices):
        OWNER = "OWNER", "Owner"
        MEMBER = "MEMBER", "Member"
        VIEWER = "VIEWER", "Viewer"

    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        related_name="memberships"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="garden_memberships"
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.MEMBER
    )

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [

            # A user can only have one membership record for a particular garden.

            # The database itself will enforce:
            #     Garden + User = unique

            # This is an example of database-level data integrity.
            models.UniqueConstraint(
                fields=["garden", "user"],
                name="unique_garden_user"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.garden.name} ({self.role})"

# garden.memberships.all()

# Previously, a simple Many-to-Many relationship could tell us:
#     mom belongs to this garden.
# But it couldn't easily tell us:
#     mom belongs to this garden as an Owner.

# >>> membership = mom.garden_memberships.get(garden=garden)
# >>> membership.role
# 'OWNER'



# Garden → Users
# garden.members.all()

# Garden → Memberships
# garden.memberships.all()

# User → Gardens
# user.gardens.all()

# User → Memberships
# user.garden_memberships.all()

























class Plant(models.Model):
    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        related_name="plants"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# ForeignKey:
# garden = models.ForeignKey(Garden, ...)
# It means: Every Plant belongs to one Garden.

# on_delete=models.CASCADE
# means: If the Garden is deleted, delete its Plants too.

# need to run # docker compose ps// to run # python manage.py makemigrations//
# modify admin.py to add plant model.
# python manage.py runserver (go to http://127.0.0.1:8000/admin/)


# garden.plants.all()
#         ↓
# Garden → Plants


# plant.garden
#         ↓
# Plant → Garden




















# Backyard Garden
# │
# ├── Plant: Tomato
# ├── Plant: Basil
# │
# ├── Task: Water tomatoes
# │     ├── Assignee: Mom
# │     ├── Due: Sept 10
# │     └── Status: To Do
# │
# ├── Task: Fertilize basil
# │     ├── Assignee: Alice
# │     ├── Due: Sept 12
# │     └── Status: In Progress
# │
# └── Task: Take garden photos
#       ├── Assignee: Bob
#       ├── Due: Sept 15
#       └── Status: Done


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        DONE = "DONE", "Done"

    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    # we need to check the plant is from the garden, not from other garden such as Grandma's Garden. 
    # We don't need to solve it immediately with complicated database constraints. We'll eventually enforce this at the API/validation layer, when we build Django REST Framework.
    # This is actually a good example of why we're building the project in stages:
    #     Database relationships first → API validation → authorization → frontend.
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="tasks"
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    assignee = models.ForeignKey(
        User,
        # Don't delete task when assignee is removed.
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO
    )

    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# User
#  │
#  ├── GardenMembership ──→ Garden
#  │                           │
#  │                           ├── Plant
#  │                           │
#  │                           └── Task ──→ User
#  │
#  └── assigned_tasks


# all tasks that aren't finished:
# Task.objects.filter(
#     garden=garden
# ).exclude(
#     status=Task.Status.DONE
# )



# At this point my database structure is:
#                     ┌──────────────┐
#                     │     User     │
#                     └──────┬───────┘
#                            │
#               ┌────────────┴────────────┐
#               │                         │
#        GardenMembership           assigned_tasks
#               │                         │
#               ↓                         ↓
#         ┌───────────┐             ┌───────────┐
#         │   Garden  │────────────→│   Task    │
#         └─────┬─────┘             └───────────┘
#               │
#               ↓
#           ┌────────┐
#           │  Plant │
#           └────────┘

# And my test data conceptually looks like:
# Garden
# │
# ├── Members
# │   ├── Mom (Owner)
# │   ├── Alice (Member)
# │   └── Bob (Viewer)
# │
# ├── Plants
# │   ├── Tomato
# │   ├── Basil
# │   └── Lettuce
# │
# └── Tasks
#     ├── Water tomatoes
#     │     ├── Plant: Tomato
#     │     └── Assignee: Mom
#     │
#     └── Water basil
#           ├── Plant: Basil
#           └── Assignee: Alice





















class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}"


# comment1 = Comment.objects.create(
#     task=task,
#     author=mom,
#     content="I watered the tomatoes this morning."
# )

# Task
#  ↓
# comments
#  ↓
# Comment
# task.comments.all()
# mom.comments.all()

# for comment in mom.comments.all():
#     print(comment.content)

# Garden
#    │
#    ├── Task
#    │     │
#    │     └── Comment
#    │            ├── author → User
#    │            └── task → Task
#    │
#    └── Plant

# Task deleted
#      ↓
# Comments deleted


# Garden
#  ├── Plants
#  │    └── Tasks
#  │         └── Comments
#  │
#  └── Tasks
#       └── Comments

# User
#  ├── Gardens
#  ├── GardenMemberships
#  ├── Assigned Tasks
#  └── Comments


    


















# Conceptually:

# User
#   │
#   │ performed
#   ▼
# Activity
#   │
#   ├── Garden
#   │
#   ├── Action
#   │
#   ├── Description
#   │
#   └── Timestamp

# For example:

# Garden: Backyard Garden
# User: Mom
# Action: COMPLETED_TASK
# Description: Completed "Water the tomatoes"
# Time: September 9, 2026 5:30 PM

# Garden
#  └── Activity
#       ├── user
#       ├── action
#       ├── description
#       └── created_at

class Activity(models.Model):
    class Action(models.TextChoices):
        CREATED_GARDEN = "CREATED_GARDEN", "Created Garden"
        ADDED_PLANT = "ADDED_PLANT", "Added Plant"
        CREATED_TASK = "CREATED_TASK", "Created Task"
        COMPLETED_TASK = "COMPLETED_TASK", "Completed Task"
        ADDED_COMMENT = "ADDED_COMMENT", "Added Comment"

    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        related_name="activities"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="activities"
    )

    action = models.CharField(
        max_length=30,
        choices=Action.choices
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.description}"



# the newest activity first. 
# -created_at = descending order → newest first.
# garden.activities.order_by("-created_at")

# How can I connect activity with actual task creation? It's not automatic.
# Later, when we build the API, we'll make the application automatically create activities:
    # POST /tasks/
    #        ↓
    # Task created
    #        ↓
    # Activity automatically created
# and:
    # PATCH /tasks/5/
    #        ↓
    # Task becomes DONE
    #        ↓
    # Activity automatically created










# Phase 3   Database relationships
# Phase 4   Django REST Framework APIs