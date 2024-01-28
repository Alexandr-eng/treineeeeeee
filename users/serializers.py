from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token

from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, \
    AuthUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'type', 'password']
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            type=validated_data['type'],
        )

        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


class LoginUserSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    class Meta:
        model = User
        fields = ['username', 'password']