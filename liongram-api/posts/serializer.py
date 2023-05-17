from rest_framework.serializers import ModelSerializer

from . import models

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'
        depth = 1

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
            'created_at',
            'view_count',
            'writer',
        ]

class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
        ]

class PostDeleteModelSerializer(PostBaseModelSerializer):
    pass
