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
# because the Activity is already being displayed inside a particular Garden.
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
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











