from rest_framework.views import APIView
from rest_framework.response import Response

def get(request):
    return Response({"message": "Salom, bu DRF API!"})

class HelloAPIView(APIView):
    pass
