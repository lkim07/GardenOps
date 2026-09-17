from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (Garden, Plant, GardenMembership, Task, Comment, Activity)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class GardenMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GardenMembership
        fields = ["id", "user", "role"]

# Garden
#   ↓
# GardenSerializer
#   ↓
#  ┌───────────────┬────────────────────┐
#  ↓               ↓
# Plants       Memberships
#  ↓               ↓
# Plant       GardenMembership
#                  ↓
#               User












class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "task",
            "author",
            "content",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["task"]










# Garden
#  └── Tasks
#       ├── Water tomatoes
#       │    └── Comments
#       │         ├── Mom
#       │         └── Alice
#       │
#       └── Water basil
#            └── Comments
class TaskSerializer(serializers.ModelSerializer):

    # due to: task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments"),
    # so task.comments.all() exists.
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "garden",
            "title",
            "description",
            "assignee",
            "status",
            "due_date",
            "plant",
            "created_at",
            "updated_at",
            "comments",
        ]







# don't include garden,
# because the Activity is already being displayed inside a particular Garden. ---- ? added garden just in case
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
            "garden",
            "user",
            "action",
            "description",
            "created_at",
        ]











class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ["id", "name", "garden"]


class GardenSerializer(serializers.ModelSerializer):

    # many=True: A garden can have multiple plants
    # read_only=True: creating or modifing plants through the Garden endpoint is not allowed.
    plants = PlantSerializer(many=True, read_only=True)


#     Your reverse relationships are:
        # Garden
        #  ├── plants
        #  ├── tasks
        #  ├── memberships
        #  └── activities

        # Task
        #  └── comments
    memberships = GardenMembershipSerializer(
        # source="gardenmembership_set",
        many=True,
        read_only=True
    )

    tasks = TaskSerializer(many=True, read_only=True)

    # comments = CommentSerializer(
    #     source="tasks__comments",     This isn't the right way to create a nested collection.
    #     many=True,
    #     read_only=True
    # )

    # activities = ActivitySerializer(
    #     many=True,
    #     read_only=True
    # )
    activities = ActivitySerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Garden
        fields = [
            "id",
            "name",
            "description",
            "plants",
            "memberships",
            "tasks",
            "activities",
        ]

# GardenSerializer(garden)
# serializer = GardenSerializer(Garden.objects.all(), many=True)
# serializer.data


# API structure:
# Garden
#  └── Tasks
#       └── Comments










# Phase 4 — Django REST Framework

# 4.1  DRF setup                         ✅
# 4.2  Serializers                       ✅
# 4.3  First API view                    ✅
# 4.4  URL routing                       ✅
# 4.5  Garden list                       ✅
# 4.6  Garden detail                     ✅
# 4.7  Garden CRUD                       ✅
# 4.8  Relationships                     ✅

# 4.9.1  Plant API                     ✅
# 4.9.2  Task CRUD API                 ✅
# 4.9.3  Comment API                   ✅
# 4.10.1 Activity Serializer          ✅
# 4.10.2 Global Activity API           ✅
# 4.10.3 Garden Activity API           ✅
# 4.10.4 Activity ordering             ✅
# 4.10.5 Activity testing              ← finish these tests

# 4.11 Validation & permissions          ⏳
# (
# 4.11.1 Proper 404 handling
# 4.11.2 Serializer validation
# 4.11.3 ForeignKey validation
# 4.11.4 HTTP status codes
# 4.11.5 Garden membership permissions
# 4.11.6 Owner / Member / Viewer rules
# 4.11.7 Protecting API endpoints
# 4.11.8 Permission testing
# 4.11.9 Error-response consistency
# )

# 4.12 API testing & refactoring         ⏳
# (
# 4.12.1 API test structure
# 4.12.2 Garden API tests
# 4.12.3 Plant API tests
# 4.12.4 Task API tests
# 4.12.5 Comment API tests
# 4.12.6 Activity API tests
# 4.12.7 Error-case tests
# 4.12.8 Relationship tests
# 4.12.9 Refactor repeated API code
# 4.12.10 Final Phase 4 verification
# )




