from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    session_id = serializers.CharField(required=True)
    user_input = serializers.CharField(required=True)