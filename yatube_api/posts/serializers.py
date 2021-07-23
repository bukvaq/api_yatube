from rest_framework import serializers

from .models import Post, Comment, Group


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов,
    дату автора и id можно только получить."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'image', 'group', 'author')
        read_only_fields = ('id', 'pub_date', 'author')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""
    class Meta:
        model = Group
        fields = ('id', 'slug', 'title', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев,
    дату автора и id можно только получить."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'created', 'author')
        read_only_fields = ('id', 'created', 'author')
