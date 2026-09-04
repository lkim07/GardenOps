from django.db import models


class Garden(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# .\.venv\Scripts\Activate.ps1

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