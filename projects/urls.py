from rest_framework import routers
from .views import ProjectViewSet, ContributorViewSet

router = routers.SimpleRouter()
router.register("projects", ProjectViewSet)
router.register("contributors", ContributorViewSet)

urlpatterns = router.urls
