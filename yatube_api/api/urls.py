from django.urls import include, path
from rest_framework import routers

from api.views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowViewSet
)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename="follow")
router.register(r'posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet,
                basename="comments")
router.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments/(?P<comment_id>[1-9]\d*)',
    CommentViewSet, basename="comment"
)


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
