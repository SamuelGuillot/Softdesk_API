from rest_framework import serializers
from projects.models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    contributors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username"
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "type",
            "author",
            "contributors",
            "created_time",
        )
        read_only_fields = ("created_time", "contributors", "author")


class ContributorSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.username")

    project = serializers.ReadOnlyField(source="project.title")

    class Meta:
        model = Contributor
        fields = (
            "user",
            "project",
            "created_time",
        )
        read_only_fields = (
            "created_time",
            "project",
        )
