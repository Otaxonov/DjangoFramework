from django.urls import path
from .views import (
    HomeView,
    PostsListView,
    PostCreateView,
    MyPostsView,
    PostDetailView,
    UserPostsView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', HomeView, name='blog_home'),
    path('posts/', PostsListView.as_view(), name='blog_posts'),
    path('post/create/', PostCreateView.as_view(), name='blog_post_create'),
    path('my/posts/', MyPostsView.as_view(), name='blog_my_posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog_post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog_post_delete'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='blog_post_detail'),
    path('user/<str:username>/posts/', UserPostsView.as_view(), name='blog_user_post'),
]