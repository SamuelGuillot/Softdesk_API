from rest_framework import routers
from .views import ProjectViewSet, ContributorViewSet

router = routers.SimpleRouter()
router.register("projects", ProjectViewSet, basename="projects")
router.register("contributors", ContributorViewSet, basename="contributors")

urlpatterns = router.urls
