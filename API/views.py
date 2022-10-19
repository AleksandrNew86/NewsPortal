from News.models import *
from rest_framework import serializers


#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#         # fields = ['name_category']

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#         # fields = ['author']

class PostSerializer(serializers.ModelSerializer):
    category_post = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ['author', 'type_post', 'category_post', 'title_post', 'text_post', ]
#views.py
from rest_framework import viewsets
from rest_framework import permissions
import django_filters

from News.models import *
from .serializers import *



class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ["type_post"]


    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (permissions.AllowAny,)
        else:
            permission_classes = (permissions.IsAuthenticated,)
        return [permission() for permission in permission_classes]


    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (permissions.AllowAny,)
        else:
            permission_classes = (permissions.IsAuthenticated,)
        return [permission() for permission in permission_classes]
