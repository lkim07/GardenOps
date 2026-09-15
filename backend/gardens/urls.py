from django.urls import path

from .views import (garden_list, garden_detail, plant_list, plant_detail,task_list, )


urlpatterns = [
    path("gardens/", garden_list, name="garden-list"),
    path("gardens/<int:garden_id>/", garden_detail, name="garden-detail"),
    
    path("plants/", plant_list, name="plant-list"),
    path("plants/<int:plant_id>/", plant_detail, name="plant-detail"),

    path("tasks/", task_list, name="task-list"),
]

# http://127.0.0.1:8000/api/gardens/
# config/urls.py
#         ↓
#     /api/
#         ↓
# gardens/urls.py
#         ↓
#     /gardens/



# the architecture used by real backend applications:
# Database
#    ↓
# Model
#    ↓
# Serializer
#    ↓
# View
#    ↓
# URL
#    ↓
# HTTP API

# ////
# Browser
#    ↓
# URL
#    ↓
# DRF View
#    ↓
# Django ORM
#    ↓
# PostgreSQL
#         ↓
#     Serializer
#         ↓
#      Response
#         ↓
#       Browser






# | Subphase | Topic                     | What you'll learn                             |
# | -------- | ------------------------- | --------------------------------------------- |
# | **4.1**  | DRF setup                 | Install/configure Django REST Framework       |
# | **4.2**  | Serializers               | Model → API data, validation                  |
# | **4.3**  | First API view            | `@api_view`, `Response`                       |
# | **4.4**  | URL routing               | Connect URLs → views                          |
# | **4.5**  | Garden list API           | `GET /api/gardens/`                           |
# | **4.6**  | Garden detail API         | `GET /api/gardens/<id>/`                      |
# | **4.7**  | Garden CRUD               | `POST`, `PUT/PATCH`, `DELETE`                 |
# | **4.8**  | Relationships             | GardenMembership, Plant, Task relationships   |
# | **4.9**  | Task & Comment APIs       | Build the core GardenOps workflow APIs        |
# | **4.10** | Activity API              | Garden activity/history                       |
# | **4.11** | Validation & permissions  | Invalid data, ownership/roles, API errors     |
# | **4.12** | API testing & refactoring | Test endpoints and clean up the API structure |


# Phase 1
# Django fundamentals

# Phase 2
# PostgreSQL + Docker

# Phase 3
# Data modeling / business logic

# Phase 4
# DRF / REST APIs


# Phase 5
# React + TypeScript

# Phase 6
# Authentication + Authorization

# Phase 7
# Testing / QA

# Phase 8
# Dockerization

# Phase 9
# CI/CD

# Phase 10
# AWS deployment


# 4. ⭐ 새로운 Phase 11 — Production Engineering
# (이게 GardenOps를 "학생 프로젝트"에서 "production-minded project"로 바꾸는 핵심이야.)
# 11.1 — API Error Handling
# 11.2 — API Validation
# ⭐ 11.3 — Database Transactions & Concurrency
# ⭐ 11.4 — Caching & Performance
# ⭐ 11.5 — Redis / Caching
# ⭐ 11.6 — Background Jobs
# ⭐ 11.7 — Observability
# ⭐ 11.8 — Security
# ⭐ 11.9 — API Documentation
# ⭐ 11.10 — Load / Performance Testing
# ⭐ 11.11 — Architecture Decision Records

# ⭐ Phase 12 — Real-world Engineering Simulation