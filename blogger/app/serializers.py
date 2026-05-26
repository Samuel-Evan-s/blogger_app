from rest_framework import serializers
from .models import Post
from django.core.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'likes', 'created_at']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Title must be at least 5 characters long.")
        return value
