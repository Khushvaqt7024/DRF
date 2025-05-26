from django.urls import path
from .views import HelloAPIView, UserDetailAPIView

urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello'),
    path('users/<int:pk>/', UserDetailAPIView.as_view())
]

