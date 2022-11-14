from django.urls import include, path
from rest_framework import routers

from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet)
router.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments/(?P<comment_id>[1-9]\d*)',
    CommentViewSet
)


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
