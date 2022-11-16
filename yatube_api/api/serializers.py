from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    ValidationError,
)
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Following yourself twice is not possible',
            )
        ]

    def validate(self, data):
        """Can't follow yourself."""
        if (self.context['request'].user.username
           == self.initial_data.get('following', False)):
            raise ValidationError(
                'Following yourself is not possible'
            )
        return data
