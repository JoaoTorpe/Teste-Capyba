from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import FilmeSerializer
from . models import Filme
@api_view(['GET'])

def filmes(request):
    filmes = Filme.objects.all()
    ser = FilmeSerializer(filmes,many=True)
    return Response(ser.data)