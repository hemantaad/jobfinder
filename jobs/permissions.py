from rest_framework import permissions

class JobPostPermission(permissions.BasePermission):
    message = 'Posting Jobs is restricted to owner only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.posted_by.user.id == request.user.id