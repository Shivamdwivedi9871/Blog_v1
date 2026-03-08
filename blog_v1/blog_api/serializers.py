from rest_framework import serializers
from blog_v1.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        comment_post = PostSerializer(read_only=True)

        fields = ['post', 'author', 'text', 'created_at']
        read_only_fields = ['author', 'created_at']

    def validate(self, data):
        if not data.get('text'):
            raise serializers.ValidationError('Comment cannot be empty')
        return data
