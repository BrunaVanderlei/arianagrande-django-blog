from django.urls import path
from .views import (
    HomeView,
    AboutView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CategoryListView,
    CategoryDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/novo/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/excluir/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/comentar/', CommentCreateView.as_view(), name='comment_create'),
    path('categorias/', CategoryListView.as_view(), name='category_list'),
    path('categorias/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]