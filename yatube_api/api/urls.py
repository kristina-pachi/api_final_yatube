from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'api'

router = SimpleRouter()

router.register('posts', views.PostViewSet)
router.register('groups', views.GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
router.register(
    'follow',
    views.FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
