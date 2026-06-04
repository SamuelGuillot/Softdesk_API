from rest_framework import serializers
from issues.models import Issue, Comment
from projects.models import Contributor


class IssueSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Issue
        fields = (
            "id",
            "title",
            "description",
            "project",
            "author",
            "assignee",
            "priority",
            "tag",
            "status",
            "created_time",
        )
        read_only_fields = ("created_time",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = (
            "id",
            "uuid",
            "description",
            "issue",
            "author",
            "created_time",
        )
        read_only_fields = ("created_time", "uuid")
