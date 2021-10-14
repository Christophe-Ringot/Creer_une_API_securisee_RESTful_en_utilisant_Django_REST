from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


# Create your views here.

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in ('POST')


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [UserPermission | permissions.IsAdminUser]
