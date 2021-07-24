from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly
from posts.models import Post, Group
from posts.serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs['post_id'])
        return post.comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
