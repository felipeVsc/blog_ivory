from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class author_view(APIView):
    """
    Essa rota só irá ser utilizada para a criação de novos Users para o Django Admin, vindo do form "Criar Blog".
    Ela foi desacoplada da criação do Blog para poder ser reutilizada em algum outro momento.
    """
    def post(self,request):
        new_user = User.objects.create_superuser(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )
        
        return Response(status=status.HTTP_201_CREATED)
