from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer

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
    

    