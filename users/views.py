from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from config.permissions import IsSelf

User = get_user_model()


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated(), IsSelf()]

    def list(self, request, *args, **kwargs):
        return Response(
            {"detail": "Action non autorisée"}, status=403
        )  # interdiction de request une liste
