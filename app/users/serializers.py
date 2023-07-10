from rest_framework import serializers
from .models import AuthorBlog


class AuthorBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBlog
        