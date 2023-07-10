from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Reply
from .serializers import *
from datetime import date
# Create your views here.

def posts_check_empty_and_return_status_code(queryset):
    if not queryset.exists():
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = PostSerializer(queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

class posts_get_all_from_blog_view(APIView):
    def get(self,request,id):
        queryset = Post.objects.filter(blog=id).filter(published=True)
        posts_check_empty_and_return_status_code(queryset)

class posts_find_by_id_view(APIView):
    def get(self,request,id):
        queryset = Post.objects.filter(id=id)
        posts_check_empty_and_return_status_code(queryset)


class posts_view(APIView):
    """
    Rota com POST e DELETE para realizar uma postagem. Isso também pode ser feito diretamente pelo Django Admin
    POST => Cria a postagem
    DELETE => Realiza o "arquivamento", tornando published=False
    """
    def post(self,request):
        post = Post(
            blog=request.data['blog'],
            text=request.data['text'],
            description=request.data['description'],
        )
        post.save()

        return Response(status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        queryset = Post.objects.get(id=pk)
        queryset.update(published=False)
        queryset.update(deleted_at=date.today)
 

class posts_get_like_by_id_view(APIView):
    def get(self,request,pk):
        queryset = Post.objects.get(id=pk)
        likes_qnt = queryset.likes
        return Response(data={"likes":likes_qnt},status=status.HTTP_200_OK)

class posts_like_view(APIView):
    """
    Rota para curtir uma postagem
    """
    def post(self,request):
        post_id = request.data['post']
        queryset = Post.objects.filter(id=post_id)
        likes_qnt = queryset.first().likes
        queryset.update(likes=likes_qnt+1)
        return Response(status=status.HTTP_200_OK)

class reply_find_by_id_view(APIView):
    def get(self,request,id):
        queryset = Reply.objects.filter(post=id)
        serializer = ReplySerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class reply_view(APIView):
    """
    Rota para comentar em uma postagem
    """
    def post(self,request):
        reply = Reply(
            post=Post.objects.get(id=request.data['post']),
            name=request.data['username'],
            text=request.data['text']
        )

        reply.save() 
        
        return Response(status=status.HTTP_201_CREATED)
 

class reply_get_all_view(APIView):
    def get(self,request,post_id):
        queryset = Reply.objects.filter(post=post_id)
        serializer = ReplySerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
class reply_find_by_id_view(APIView):
    def get(self,request,reply_id):
        queryset = Reply.objects.get(id=reply_id)
        serializer = ReplySerializer(queryset)
        # Fazer a checagem de vazio e etc?
        return Response(data=serializer.data,status=status.HTTP_200_OK)
 
class reply_get_likes_by_id_view(APIView):
    def get(self,request,pk):
        queryset = Reply.objects.get(id=pk).likes
        return Response(data={"likes:",queryset},status=status.HTTP_200_OK)

class reply_likes_view(APIView):
    """
    Rota para curtir um comentário
    """
    def post(self,request):
        reply_id = request.data['reply']
        queryset = Reply.objects.filter(id=reply_id)
        likes_qnt = queryset.first().likes

        queryset.update(likes=likes_qnt+1)
        return Response(status=status.HTTP_200_OK)