
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer ,UserUpdateSerializer,LoginSerializer,RegisterSerializer,ChangepassSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema,OpenApiParameter, OpenApiExample, inline_serializer, OpenApiRequest,OpenApiResponse
from django.shortcuts import get_object_or_404

@extend_schema(
    summary="Login do usuário (Lembrar do prefixo 'Token')",
    description="Sempre que for colocar o token no value do Authrize tem que por o prefixo 'Token' Ex: Token 376a5dbefd1c7f5eaca4554df4ac0cbff47",
    request=OpenApiRequest(
        request=LoginSerializer,  
        examples=[
            OpenApiExample(
                name='Exemplo de login',
                value={
                    'email': 'email@email.com',
                    'password': 'senha123'
                },
                description='Exemplo de login com email e senha'
            )
        ]
    )
)
 
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User,email=request.data['email'])

    if not user.check_password(request.data['password']):
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token":token.key})

@extend_schema(
    summary="Registro do usuário",
    description="Endpoint para registro do usuário",
    request=OpenApiRequest(
        request=RegisterSerializer,  
        examples=[
            OpenApiExample(
                name='Exemplo de registro',
                value={
                    'username':'joao',
                    'email': 'email@email.com',
                    'password': 'senha123'
                },
                description='Exemplo de registro'
            )
        ]
    )
)
@api_view(['POST'])
def register(request):
    ser = UserSerializer(data = request.data)

    if ser.is_valid():
        ser.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    summary="Logout",
    description="Esse endpoint não precisa de parametros é só executar",
    
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
   try:
       token = Token.objects.get(user=request.user)
       
       token.delete()
       return Response({"detail": "Logout realizado com sucesso."}, status=status.HTTP_200_OK)
   except Token.DoesNotExist:
       return Response({"detail": "Token não encontrado."}, status=status.HTTP_400_BAD_REQUEST)
   
@extend_schema(
    summary="Mudar senha do usuario atual",
    description="Endpoint para alterar a senha do usuario com a confirmacao da senha atual",
    request=OpenApiRequest(
        request=ChangepassSerializer,  
        examples=[
            OpenApiExample(
                name='Exemplo mudar senha',
                value={
                    'current_password': 'senha123',
                    'new_password': 'pass123'
                },
                description='Exemplo de troca de senha'
            )
        ]
    )
)
 #Muda a senha do usuario logado, com a confirmacao da senha atual  
@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def change_password(request):
    user = request.user 

   
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')
  
   
    if not user.check_password(current_password):
        return Response({"error": "A senha atual está incorreta."}, status=status.HTTP_400_BAD_REQUEST)

 
    user.set_password(new_password)
    user.save()

    return Response({"success": "A senha foi alterada com sucesso!"}, status=status.HTTP_200_OK)

@extend_schema(
    summary="Alterar dados ",
    description="Endpoint para alterar dados do usuario (Username e Email)",
    request=OpenApiRequest(
        request=ChangepassSerializer,  
        examples=[
            OpenApiExample(
                name='Exemplo de alteracao de dados',
                value={
                    'username': 'novo_username',
                    'email': 'novo@email.com'
                },
                description='Exemplo de alteracao de dados'
            )
        ]
    )
)
#Endpoint para alterar cadastro de usuario, muda o nome e o email do usuario atual
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_data(request):
    user = request.user

    ser = UserUpdateSerializer(user,request.data,partial=True)
    if ser.is_valid():
        ser.save()
        return Response(status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
