from django.urls import path, include
from b_v1.api.views import PostListCreateAPIView, PostDetailsView, CommentView
urlpatterns = [
    path('list/', PostListCreateAPIView.as_view(), name='Blog-list'),
    path('create/', PostListCreateAPIView.as_view(), name='Blog-create'),
    path('list/<int:pk>/update', PostDetailsView.as_view(), name='post-deatil'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('comment/create/', CommentView.as_view(), name='post-comment'),
    path('comment/<int:pk>/', CommentView.as_view(), name='comment-detail'),
    path('comment/<int:pk>/update/', CommentView.as_view(), name='update-comment')
]
