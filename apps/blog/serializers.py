from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "views",
        ]


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "thumbnail",
            "excerpt",
            "description",
            "time_read",
            "published",
            "views",
        ]
