from warnings import filters

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics



def get(request):
    return Response({"message": "Salom, bu DRF API!"})

class HelloAPIView(APIView):
    pass


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response


class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'Topilmadi'}, status=404)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'Topilmadi'}, status=404)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({'error': 'Topilmadi'}, status=404)
        user.delete()
        return Response({'deleted': True}, status=204)

# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

    # @action(detail=True, methods=['get'])
    # def full_name(self, request, pk=None):
    #     user = self.get_object()
    #     full_name = f"{user.first_name} {user.last_name}"
    #     return Response({'full_name': full_name})

class UserListCreateViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def get_permissions(selfs):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]


class NotificationSerializer:
    pass


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')
