from django.contrib.auth.models import User as UserAuth
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserAuth.objects.create_user(**validated_data)
        return user

class ChatSerializer(serializers.Serializer):
    session_id = serializers.CharField(required=True)
    user_input = serializers.CharField(required=True)