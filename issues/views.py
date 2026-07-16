from rest_framework.viewsets import ModelViewSet
from issues.serializers import (
    CommentDetailSerializer,
    CommentListSerializer,
    IssueDetailSerializer,
    IssueListSerializer,
)
from issues.models import Issue, Comment
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsAuthorOrReadOnly, IsContributor
from django.core.exceptions import PermissionDenied
from projects.models import Contributor, Project


# Create your views here.
class IssueViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrReadOnly,
        IsContributor,
    ]

    def get_queryset(self):
        return Issue.objects.filter(
            project_id=self.kwargs["project_pk"]
        ).select_related(
            "project",
            "author",
            "assignee",
        )

    def get_serializer_class(self):
        if self.action == "list":
            return IssueListSerializer
        return IssueDetailSerializer

    def get_project(self):
        return Project.objects.get(pk=self.kwargs["project_pk"])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["project"] = self.get_project()
        return context

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            project=self.get_project(),
        )


class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return (
            Comment.objects
            .filter(issue_id=self.kwargs["issue_pk"])
            .select_related(
                "issue",
                "author",
            )
        )

    def get_serializer_class(self):
        if self.action == "list":
            return CommentListSerializer
        else:
            return CommentDetailSerializer

    def perform_create(self, serializer):
        issue_id = self.kwargs.get("issue_pk")
        issue = Issue.objects.get(pk=issue_id)
        user = self.request.user
        project = issue.project
        is_contributor = (
            Contributor.objects
            .filter(
                project=project,
                user=user,
            )
            .exists()
        )

        if not is_contributor:
            raise PermissionDenied("Must be contributor")

        serializer.save(author=user, issue=issue)
