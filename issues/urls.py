from rest_framework import routers
from .views import IssueViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register("issues", IssueViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls
