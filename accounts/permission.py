from rest_framework.permissions import BasePermission

class IsStudentUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.role == "student":
            return True
        else:
            return False
     