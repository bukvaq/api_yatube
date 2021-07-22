from rest_framework import serializers

from .models import Post, Comment, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'image', 'group', 'author')
        read_only_fields = ('id', 'pub_date', 'author')

    def get_author(self, obj):
        return obj.author.username


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'slug', 'title', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'created', 'author')
        read_only_fields = ('id', 'created', 'author')

    def get_author(self, obj):
        return obj.author.username
