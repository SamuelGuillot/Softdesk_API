from rest_framework.viewsets import ModelViewSet
from .serializers import ContributorSerializer, ProjectSerializer
from rest_framework.exceptions import PermissionDenied
from projects.models import Project, Contributor
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsAuthorOrReadOnly


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete", "head", "options"]

    def get_queryset(self):
        return Contributor.objects.filter(
            project_id=self.kwargs["project_pk"]
        ).select_related("user", "project")

    # contributors nested under a project

    def create(self, request, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        if project.author != request.user:
            raise PermissionDenied("Only project author can add contributors.")
        return super().create(request, *args, **kwargs)
        # http layer

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project)
        # database layer

    def destroy(self, request, *args, **kwargs):
        contributor = Contributor.objects.get(pk=self.kwargs["pk"])
        if contributor.project.author != request.user:
            raise PermissionDenied(
                "Only project author can remove contributors."
            )
        return super().destroy(request, *args, **kwargs)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Project.objects.filter(
            contributors=self.request.user
        ).select_related(  # Seulement les projets auxquels il a contribué
            "author"
        )

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        project.contributors.add(self.request.user)
