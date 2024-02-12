from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow authenticate
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            # staff users to create tasks
            return request.user.role.type == 'staff' or request.user.role.type== 'admin'
        
    def has_object_permission(self, request, view, obj):
        print(request.user.role.type)
         # Allow admin to perform any action
        if request.user.role.type == 'admin':
            return True
        
        # Allow task owner to update or delete the task
        if request.user == obj.username:
            return True
        
        # Allow authenticated users to retrieve tasks
        return request.method in permissions.SAFE_METHODS