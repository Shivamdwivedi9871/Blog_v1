from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.validators import ValidationError


from blog_v1.models import Post, Comment
from blog_v1.blog_api.serializers import PostSerializer, CommentSerializer
from blog_v1.blog_api.permission import IsAuthororReadOnly, IsAdminorReadOnly


class PostView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthororReadOnly, IsAdminorReadOnly]

    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthororReadOnly, IsAdminorReadOnly]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise ValidationError(
                'You do not have permission to edit this post')
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise ValidationError(
                'You do not have permission to delete this post')
        instance.delete()


class CommentView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthororReadOnly, IsAdminorReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthororReadOnly, IsAdminorReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(pk=pk)

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise ValidationError(
                f'you don\'t have permission to edit this comment')
        return serializer.save(authore=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise ValidationError(
                f'you don\'t have permission to delete this comment')
        instance.delete()
