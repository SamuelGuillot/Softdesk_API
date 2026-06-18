from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import ContributorSerializer, ProjectSerializer
from projects.models import Project, Contributor
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsAuthorOrReadOnly


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def get_queryset(self):

        return Project.objects.filter(
            contributors__user=self.request.user
        )




class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Project.objects.filter(
            contributors=self.request.user
        ) #Seulement les porjets auquels il a contribué
    
    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        project.contributors.add(self.request.user)

    # def update(self, request, pk):
    #     project = Project.objects.get(pk=pk)
    #     if project.author != request.user:
