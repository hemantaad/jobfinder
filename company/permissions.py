from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        data = request.data
        if view.action == 'list':
            return True
            
        return request.user.user_type == "2" and int(data['user']) == request.user.id


class CompanyEditPermission(permissions.BasePermission):
    message = 'Editing company profile is restricted to user only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id
