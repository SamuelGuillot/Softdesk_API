from rest_framework import serializers
from issues.models import Issue, Comment
from projects.models import Contributor


class IssueListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Issue
        fields = ("id", "title", "status", "priority", "author")


class IssueDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    assignee_username = serializers.ReadOnlyField(source="assignee.username")

    class Meta:
        model = Issue
        fields = (
            "id",
            "title",
            "description",
            "author",
            "assignee",
            "assignee_username",
            "priority",
            "tag",
            "status",
            "created_time",
        )
        read_only_fields = (
            "created_time",
            "project",
        )

    def validate_assignee(self, value):
        project = self.context["project"]
        if not Contributor.objects.filter(
            project=project,
            user=value,
        ).exists():
            raise serializers.ValidationError(
                "Assignee must be a contributor."
            )
        return value


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ("id", "description", "author", "created_time")


class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = (
            "id",
            "uuid",
            "description",
            "author",
            "created_time",
        )
        read_only_fields = ("created_time", "uuid", "issue")
