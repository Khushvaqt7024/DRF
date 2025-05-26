from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, UserDetailAPIView, UserViewSet

# urlpatterns = [
#     path('hello/', HelloAPIView.as_view(), name='hello'),
#     path('users/<int:pk>/', UserDetailAPIView.as_view())
# ]

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls