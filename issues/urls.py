from rest_framework import routers
from django.urls import path
from .views import IssueViewSet, CommentViewSet
from . import views

router = routers.SimpleRouter()
router.register("issues", IssueViewSet, basename="issues")
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = router.urls



# urlpatterns = [
#     path("issues/", views.issue_list),
#     path("issues/<int:issue_id>/", views.issue_detail),

#     path("issues/<int:issue_id>/comments/", views.comment_list),
#     path("issues/<int:issue_id>/comments/<int:comment_id>/", views.comment_detail),
# ]