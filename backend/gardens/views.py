# from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Garden, Plant, Task, Comment, Activity
from .serializers import (GardenSerializer, PlantSerializer, TaskSerializer, CommentSerializer, ActivitySerializer, GardenMembership)

from django.shortcuts import get_object_or_404

# @api_view(["GET"])
# def garden_list(request):
#     gardens = Garden.objects.all()
#     serializer = GardenSerializer(gardens, many=True)

#     return Response(serializer.data)
@api_view(["GET", "POST"])
def garden_list(request):
    if request.method == "GET":
        gardens = Garden.objects.all()
        serializer = GardenSerializer(gardens, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = GardenSerializer(data=request.data)

        if serializer.is_valid():
            garden = serializer.save()
            return Response(
                GardenSerializer(garden).data,
                status=201
            )

        return Response(serializer.errors, status=400)

# POST request
#     ↓
# DRF View
#     ↓
# Serializer validation
#     ↓
# serializer.save()
#     ↓
# Django ORM
#     ↓
# PostgreSQL

















# @api_view(["GET"])
# def garden_detail(request, garden_id):
#     garden = Garden.objects.get(id=garden_id)
#     serializer = GardenSerializer(garden)

#     return Response(serializer.data)

# PATCH request
#       ↓
# garden_detail()
#       ↓
# GardenSerializer
#       ↓
# is_valid()
#       ↓
# serializer.save()
#       ↓
# PostgreSQL UPDATE

# ex: 
# PATCH /api/gardens/2/
# DELETE /api/gardens/2/
# http://127.0.0.1:8000/api/gardens/2/
@api_view(["GET", "PATCH", "DELETE"])
def garden_detail(request, garden_id):

    # garden = Garden.objects.get(id=garden_id)
    # For handling Garden.DoesNotExist, 
    garden = get_object_or_404(Garden, id=garden_id)

    if request.method == "GET":
        serializer = GardenSerializer(garden)
        return Response(serializer.data)

    elif request.method == "PATCH":
        serializer = GardenSerializer(
            garden,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            garden = serializer.save()
            return Response(GardenSerializer(garden).data)

        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        garden.delete()
        return Response(status=204)



# PostgreSQL
#     ↓
# Django Model
#     ↓
# Serializer
#     ↓
# API View
#     ↓
# URL
#     ↓
# Browser / API client



# Phase 4.7 CRUD API
# GET     /api/gardens/
# GET     /api/gardens/<id>/
# POST    /api/gardens/
# PATCH   /api/gardens/<id>/
# DELETE  /api/gardens/<id>/














# Database
#    ↓
# Plant.objects.all()
#    ↓
# PlantSerializer
#    ↓
# Response
#    ↓
# JSON
@api_view(["GET"])
def plant_list(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def plant_detail(request, plant_id):
    # plant = Plant.objects.get(id=plant_id)
    plant = get_object_or_404(Plant, id=plant_id)
    serializer = PlantSerializer(plant)

    return Response(serializer.data)
















# GET
#  ↓
# retrieve objects
#  ↓
# serialize
#  ↓
# Response

# POST
#  ↓
# request.data
#  ↓
# serializer validation
#  ↓
# serializer.save()
#  ↓
# Response

@api_view(["GET", "POST"])
def task_list(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            task = serializer.save()

            return Response(
                TaskSerializer(task).data,
                status=201
            )

        return Response(serializer.errors, status=400)


@api_view(["GET", "PATCH", "DELETE"])
def task_detail(request, task_id):
    # task = Task.objects.get(id=task_id)
    task = get_object_or_404(Task, id=task_id)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == "PATCH":
        serializer = TaskSerializer(
            task,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            task = serializer.save()

            return Response(
                TaskSerializer(task).data
            )

        return Response(
            serializer.errors,
            status=400
        )

    elif request.method == "DELETE":
        task.delete()

        return Response(status=204)

# Garden API already follows this pattern:

# GET
#  ↓
# retrieve object
#  ↓
# serialize
#  ↓
# return response

# For PATCH:

# existing object
#       ↓
# request.data
#       ↓
# serializer validation
#       ↓
# save()
#       ↓
# updated object

# For DELETE:

# existing object
#       ↓
# delete()
#       ↓
# 204 No Content







@api_view(["GET", "POST"])
def task_comment_list(request, task_id):
    # task = Task.objects.get(id=task_id)
    task = get_object_or_404(Task, id=task_id)

    if request.method == "GET":
        comments = task.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            comment = serializer.save(task=task)

            return Response(
                CommentSerializer(comment).data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )










@api_view(["GET"])
def activity_list(request):
    activities = Activity.objects.all().order_by("-created_at")
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)




@api_view(["GET"])
def garden_activity_list(request, garden_id):
    # garden = Garden.objects.get(id=garden_id)
    garden = get_object_or_404(Garden, id=garden_id)

    activities = Activity.objects.filter(
        garden=garden
    ).order_by("-created_at")

    serializer = ActivitySerializer(
        activities,
        many=True
    )

    return Response(serializer.data)








# At this point, API should conceptually look like this:
# GardenOps API
# │
# ├── gardens/
# │   ├── GET
# │   ├── POST
# │   └── <garden_id>/
# │       ├── GET
# │       ├── PATCH
# │       ├── DELETE
# │       └── activities/
# │           └── GET
# │
# ├── plants/
# │   ├── GET
# │   └── <plant_id>/
# │       └── GET
# │
# ├── tasks/
# │   ├── GET
# │   ├── POST
# │   └── <task_id>/
# │       ├── GET
# │       ├── PATCH
# │       └── DELETE
# │
# ├── tasks/<task_id>/comments/
# │   ├── GET
# │   └── POST
# │
# └── activities/
#     └── GET









# helper functions
def get_membership(user, garden):
    return GardenMembership.objects.filter(
        user=user,
        garden=garden
    ).first()

def has_role(user, garden, allowed_roles):
    membership = get_membership(user, garden)

    if not membership:
        return False

    return membership.role in allowed_roles
