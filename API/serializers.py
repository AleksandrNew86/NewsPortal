from News.models import *
from rest_framework import serializers


#
#
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['name_category']

# class AuthorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['author']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()
    category_post = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ['author', 'type_post', 'category_post', 'title_post', 'text_post', ]

