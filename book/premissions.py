from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    
     def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser or request.user.is_staff:
            return True

        return obj == request.user

    
    #def has_object_permission(self, request, obj,view):
     #   if request.method in permissions.SAFE_METHODS:
      #      print(request.method)
       #     return True
           
        #return request.user.is_superuser or request.user.is_staff == True