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