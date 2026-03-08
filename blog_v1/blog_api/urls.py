from django.urls import path, include
from blog_v1.blog_api.views import (
    PostView, PostDetailView, CommentView, CommentDetailView)

urlpatterns = [

    path('post/', PostView.as_view(), name='create-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/', CommentView.as_view(), name='Comments'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
