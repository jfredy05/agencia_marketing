from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Category, Post, ViewCountPost
from .serializers import PostSerializer


class ListCategoriesView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, format=None):
        if Category.objects.all().exists():
            categories = Category.objects.all()
            
            result = []
            return Response(
                {
                    "categories": "test message"
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "No categories found"
                },
                status=status.HTTP_400_NOT_FOUND
            )


class BlogListView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, format=None):
        if Post.objects.all().exists():
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(
                {
                    "posts": serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "Not posts found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
