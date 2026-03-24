from rest_framework import serializers
from b_v1.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created', 'updated']
        read_only_fields = ['author']


class CommentSerializer(serializers.ModelSerializer):
    post_detail = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'post_detail']
        read_only_fields = ['author', 'created']

    def validate(self, data):
        if not data.get('content'):
            return serializers.ValidationError('Comment cannot be empty')
        return data
