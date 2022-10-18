from rest_framework import viewsets
from rest_framework import permissions
import django_filters

from News.models import *
from .serializers import *

# class AuthorViewset(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class CategoryViewset(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["type_post"]


    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (permissions.AllowAny,)
        else:
            permission_classes = (permissions.IsAuthenticated,)
        return [permission() for permission in permission_classes]
