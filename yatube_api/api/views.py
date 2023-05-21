from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)
from .permissions import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    """
    Работает с эндпоинтами для модели Post,
    обрабатывает запросы к API,
    поддерживает все CRUD-операции.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Работает с эндпоинтами для модели Group,
    обрабатывает только GET запросы к API.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Работает с эндпоинтами для модели Comment,
    обрабатывает запросы к API,
    поддерживает все CRUD-операции.
    """

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(
            author=self.request.user,
            post=post,
        )


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Работает с эндпоинтом для модели Follow,
    обрабатывает GET и POST запросы к API.
    """

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,)
