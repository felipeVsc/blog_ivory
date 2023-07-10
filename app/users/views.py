from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AuthorBlog
from .serializers import AuthorBlogSerializer
# Create your views here.
from django.contrib.auth.models import User, Permission
    
from django.contrib.auth import get_user_model
User = get_user_model()

class author_find_by_id_view(APIView):
    def get(self,request,pk):
        queryset = AuthorBlog.objects.get(id=pk)
        serializer = AuthorBlogSerializer(queryset)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
        

class author_view(APIView):
    def get(self,request):
        queryset = AuthorBlog.objects.all()
        serializer = AuthorBlogSerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
       
        newUser = User.objects.create_superuser(
            username=request.data['name'],
            email=request.data['email'],
            password=request.data['password']
        )
        
        
        return Response(status=status.HTTP_201_CREATED)# add return

    def update(self,request):
        pass

    def delete(self,request):
        pass
