from rest_framework import serializers
from .models import Thread
from accounts.models import User

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'profile_color']

class ThreadSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)
    class Meta:
        model = Thread
        fields = ['id', 'user', 'title', 'content', 'created_at']
