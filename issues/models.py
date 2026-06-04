import uuid

from django.conf import settings
from django.db import models

from projects.models import Project


class Issue(models.Model):

    class Priority(models.TextChoices):
        LOW = "Low"
        MEDIUM = "Medium"
        HIGH = "High"

    class Element(models.TextChoices):
        BUG = "Bug"
        FEATURE = "Feature"
        TASK = "Task"

    class Status(models.TextChoices):
        TODO = "To Do"
        IN_PROGRESS = "In Progress"
        FINISHED = "Finished"

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="issues",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authored_issues",
    )

    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_issues",
    )

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.LOW,
    )

    tag = models.CharField(
        max_length=10,
        choices=Element.choices,
        default=Element.TASK,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )

    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    description = models.TextField()

    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    created_time = models.DateTimeField(auto_now_add=True)
