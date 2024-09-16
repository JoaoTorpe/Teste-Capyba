from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import FilmeSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import Filme
from .CustomPagination import CustomPagination


@extend_schema(
    summary="Listagem de filmes",
    description="Endpoint para listar filmes com suporte a busca, filtro por premiado e ordenação.",
    parameters=[
         OpenApiParameter(
            name='page',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Decide qual pagina sera listada (Precisa definir o page_size para funcionar)',
            required=False,
            
        ),
        OpenApiParameter(
            name='page_size',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Numero de itens por pagina (paginação)',
            required=False,
            
        ),
        OpenApiParameter(
            name='search',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Busca pelo titulo ou genero do filme',
            required=False
        ),
        OpenApiParameter(
            name='premiado',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Filtrar por filmes premiados (True/False)',
            required=False
        ),
        OpenApiParameter(
            name='ordering',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Ordenar por titulo ou ano de lançamento ("titulo" ou "ano_de_lancamento")',
            required=False
        ),
    ],
    responses={
        200: FilmeSerializer(many=True)
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filmes(request):
   #Tamanho da pagina para paginacao
   page_size = request.query_params.get('page_size', None)
   # parametro de search, que vai buscar no titulo e no genero do filme
   search = request.query_params.get('search',None)
   # paramentro booleano que filtra por filmes premiados ou nao
   is_premiado = request.query_params.get('premiado',None)
   # Ordenar por titulo ou por ano_de_lancamento
   ordering = request.query_params.get('ordering',None)


   filmes = Filme.objects.all() 
   ser = FilmeSerializer(filmes,many=True)
   total_de_objetos = Filme.objects.count() 

    #Verificando a existencia dos parametros


   if search:
      filmes = filmes.filter(titulo__icontains=search) | filmes.filter(genero__icontains=search)     
      
   if ordering:
      filmes = filmes.order_by(ordering) 

   if is_premiado != None:
      filmes = filmes.filter(premiado = is_premiado)   

   if page_size:
   
    pagination = CustomPagination()
    filmes =pagination.paginate_queryset(filmes, request)   
    
   ser = FilmeSerializer(filmes,many=True) 
   return Response({ "Total de itens na base de dados":total_de_objetos , "response": ser.data})