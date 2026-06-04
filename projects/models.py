from django.conf import settings
from django.db import models


class Project(models.Model):

    class ProjectType(models.TextChoices):
        BACKEND = "Back-end"
        FRONTEND = "Front-end"
        IOS = "iOS"
        ANDROID = "Android"

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    type = models.CharField(
        max_length=20,
        choices=ProjectType.choices,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_projects",
    )

    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Contributor",
        related_name="projects",
    )

    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributions",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project_contributors",
    )

    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "project")
