from rest_framework.permissions import BasePermission

class ReadOnlyOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return request.user and request.user.is_superuser