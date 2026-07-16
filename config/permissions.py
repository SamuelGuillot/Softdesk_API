from rest_framework.permissions import BasePermission
from projects.models import Contributor


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == "GET":
            return True

        return obj.author == request.user


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsContributor(BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_pk")

        return Contributor.objects.filter(
            project_id=project_id,
            user=request.user,
        ).exists()
