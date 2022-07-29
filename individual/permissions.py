from rest_framework import permissions

from individual.models import IndividualProfile


class IsIndividual(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        else:
            def has_object_permission(self, request, view, obj):
                return obj.user.id == request.user.id and request.user.user_type == "1"

class IsIndividualProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == "1":
            profile = IndividualProfile.objects.get(user_id=request.user.id)
            print(profile.profile_type)
            if profile.profile_type == "2" or profile.profile_type == "3": 
                return True
            else:
                return False
        else:
             return False


class IndividualProfileEditPermission(permissions.BasePermission):
    message = 'Editing Profile is restricted to user only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id
