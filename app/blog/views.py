from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from django.contrib.auth.models import User
import time
class blogs_find_by_id_view(APIView):
    def get(self,request,pk):
        queryset = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(queryset)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class blogs_view(APIView):
    def get(self,request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        time.sleep(1)
        author = User.objects.get(username=request.data['username'])
        new_blog = Blog(
            author=author,
            name=request.data['name'],
            description=request.data['description']
        )

        new_blog.save()

        return Response(status=status.HTTP_200_OK)

    