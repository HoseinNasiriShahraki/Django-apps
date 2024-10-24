from rest_framework import serializers
from django.contrib.auth.models import User #Base Django User Model
# from .models import User  ## Custom User Model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude: list = [
            "password",
            "email",
            "groups",
            "is_staff",
            "is_superuser",
            "is_active",
        ]
        extra_kwargs = {"url": {"view_name": "user-detail", "lookup_field": "username"}}


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: list = ["username", "password", "email", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token

