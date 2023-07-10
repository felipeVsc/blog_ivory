from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Reply
from .serializers import *
from datetime import date
# Create your views here.

class posts_get_all_from_blog_view(APIView):
    def get(self,request,id):
        queryset = Post.objects.filter(blog=id).filter(published=True)
        serializer = PostSerializer(queryset,many=True)
        # Fazer a checagem de vazio e etc?
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class posts_find_by_id_view(APIView):
    def get(self,request,id):
        queryset = Post.objects.filter(id=id).first()
        serializer = PostSerializer(queryset)
        # Fazer a checagem de vazio e etc?
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class posts_view(APIView):
    def post(self,request):
        post = Post(
            blog=request.data['blog'],
            text=request.data['text'],
            description=request.data['description'],
        )
        post.save()

        return Response(status=status.HTTP_200_OK)
    
    def update(self,request):
        pass

    def delete(self,request,pk):
        queryset = Post.objects.get(id=pk)
        queryset.update(published=False)
        queryset.update(deleted_at=date.today)
 

class posts_get_like_by_id_view(APIView):
    def get(self,request,pk):
        queryset = Post.objects.get(id=pk)
        likes_qnt = queryset.likes
        serializer = PostSerializer(queryset)
        # Fazer a checagem de vazio e etc?
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class posts_like_view(APIView):

    def put(self,request):
        post_id = request.data['post']
        queryset = Post.objects.filter(id=post_id)
        likes_qnt = queryset.first().likes
        queryset.update(likes=likes_qnt+1)
        return Response(status=status.HTTP_200_OK)



class reply_view(APIView):
    def get(self,request,pk):
        queryset = Reply.objects.filter(post=pk)
        serializer = ReplySerializer(queryset,many=True)
        # Fazer a checagem de vazio e etc?
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        reply = Reply(
            post=Post.objects.get(id=request.data['post']),
            name=request.data['name'],
            text=request.data['text']
        )

        reply.save() 
        
        return Response(status=status.HTTP_201_CREATED)
 

class reply_find_by_id_view(APIView):
    def get(self,request,pk):
        queryset = Reply.objects.get(id=pk)
        serializer = ReplySerializer(queryset)
        # Fazer a checagem de vazio e etc?
        return Response(data=serializer.data,status=status.HTTP_200_OK)
 
class reply_get_likes_by_id_view(APIView):
    def get(self,request,pk):
        queryset = Reply.objects.get(id=pk).likes
        return Response(data={"likes:",queryset},status=status.HTTP_200_OK)

class reply_likes_view(APIView):
    def put(self,request):
        replyid = request.data['reply']
        queryset = Reply.objects.filter(id=replyid)
        print(queryset)
        likes_qnt = queryset.first().likes
        queryset.update(likes=likes_qnt+1)

        return Response(status=status.HTTP_200_OK)