from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'PUT', 'DELETE', 'PATCH']:
            return True
        return obj.user == request.user
