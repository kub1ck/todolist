from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password", "password_repeat")

    def validate(self, attrs):
        if attrs.get("password") != attrs.pop("password_repeat"):
            raise ValidationError("Passwords must match!")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user


class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        user = authenticate(username=validated_data["username"], password=validated_data["password"])

        if not user:
            raise ValidationError("Username or password is incorrect!")

        return user


class UpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ("old_password", "new_password")

    def validate(self, attrs):
        user = self.instance

        if not user.check_password(attrs.get("old_password")):
            raise ValidationError({"old_password": "password is incorrect"})

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save(update_fields=["password"])

        return instance
