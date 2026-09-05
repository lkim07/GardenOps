from django.db import models


class Garden(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

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