from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

   def has_object_permission(self, request, view, obj):
       """
       Проверка владельца объекта
       """
       if obj.author == request.user:
           return True
       return False

class IsAdmin(BasePermission):

   def has_object_permission(self, request, view, obj):
       """
       Проверка пользователя на админа
       """
       if request.user.role == "admin":
           return True
       return False