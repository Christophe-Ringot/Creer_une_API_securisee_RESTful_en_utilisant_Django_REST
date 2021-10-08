from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
