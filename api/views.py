
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def login(request):
    return Response({"login"})

@api_view(['POST'])
def register(request):
    return Response({"register"})


@api_view(['POST'])
def validate_token(request):
    return Response({"validate"})