from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.user.role == 'admin':
            return True
        
        if obj.owner == request.user:
            return True