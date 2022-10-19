from News.models import *
from rest_framework import serializers





class PostSerializer(serializers.ModelSerializer):
    category_post = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ['author', 'type_post', 'category_post', 'title_post', 'text_post', ]

