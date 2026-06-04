from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "can_be_contacted",
            "can_data_be_shared",
            "date_joined",
            "password",
        )

    def validate_age(self, value):
        if value is not None and value < 15:
            raise serializers.ValidationError(
                "L'utilisateur doit avoir au moins 15 ans pour s'inscrire."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            age=validated_data.get("age"),
            can_be_contacted=validated_data.get("can_be_contacted", False),
            can_data_be_shared=validated_data.get("can_data_be_shared", False),
        )
        return user
