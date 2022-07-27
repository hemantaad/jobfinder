from rest_framework import permissions


class IsSeeker(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return request.user.user_type == "1"


class SeekerProfileEditPermission(permissions.BasePermission):
    message = 'Editing Profile is restricted to user only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id
