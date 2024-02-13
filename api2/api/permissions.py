from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user.role.type=='staff' or request.user.role.type=='admin'
        
        return False
    def has_object_permission(self, request, view, obj):

        if request.user.role.type=='admin':
            return True
        if request.user == obj.username:
            return True
        return request.method in permissions.SAFE_METHODS
    