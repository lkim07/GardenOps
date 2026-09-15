# from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Garden, Plant, Task
from .serializers import (GardenSerializer, PlantSerializer, TaskSerializer)


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
    garden = Garden.objects.get(id=garden_id)

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
    plant = Plant.objects.get(id=plant_id)
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