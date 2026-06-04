from rest_framework import serializers
from projects.models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source="author.username")

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
        read_only_fields = ("created_time", "contributors")


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = (
            "id",
            "user",
            "project",
            "created_time",
        )
        read_only_fields = ("created_time",)
