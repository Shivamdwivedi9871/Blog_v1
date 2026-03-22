from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import filters
from rest_framework.throttling import AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from b_v1.models import Post, Comment
from b_v1.api.serializer import PostSerializer, CommentSerializer
from b_v1.api.permission import IsAuthorOrReadOnly
from b_v1.api.throttle import PostViewThrottle, PostDetailThrottle
from b_v1.api.pagination import ResultPerPage, ResultLimitOffSet, ResultCursorPage, CommentViewPage


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    throttle_classes = [PostViewThrottle, AnonRateThrottle]
    pagination_class = ResultPerPage
    # throttle_scope = 'blog-list'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailsView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    throttle_classes = [PostDetailThrottle, AnonRateThrottle]
    pagination_class = ResultCursorPage
    # throttle_scope = 'post-detail'
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'created']
    search_fields = ['title', 'content']
    ordering_fields = ['created']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_update(self, serializer):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']

        author = self.request.user
        queryset = Post.objects.filter(author=author)

        # if queryset.exists():
        #     raise ValidationError('User already Posted the Blog')

        serializer.save(author=author)

    def perform_destroy(self, instance):
        # if self.request.user != instance.author:
        #     raise ValidationError(
        #         'You Don\'t have permission to delete this post!')
        instance.delete()


class CommentView(generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = CommentViewPage

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
