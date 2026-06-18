from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from issues.serializers import IssueSerializer, CommentSerializer
from issues.models import Issue, Comment
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from config.permissions import IsAuthorOrReadOnly

# Create your views here.
class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Issue.objects.filter(
            project__contributors=self.request.user
        )
        # problème visible par tous les contributeurs du projet

    def perform_create(self, serializer):
        # serializer.save(author_id=1)
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # serializer.save(author_id=1)
        serializer.save(author=self.request.user)


