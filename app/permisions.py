from rest_framework.permissions import BasePermission, SAFE_METHODS


class CourseAndProfileUpdatePermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        try:
            if obj.user == request.user:
                return True
        except:
            pass
        
        try:
            if obj.course.user == request.user:
                return True
        except:
            pass
        
        try:
            if obj.user.is_superuser == True:
                return True
        except:
            pass

# Bu permision kurslar, video va darslarni faqar superuserlar yarata olishi haqida 

class CreatePermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        try:
            if obj.user.is_superuser == True:  # Bu superuserlikga tekshiradi yani adminlikga
                return True
        except:
            return False

        