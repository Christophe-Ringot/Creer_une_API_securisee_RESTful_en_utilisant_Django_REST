from rest_framework import routers

from projects.views import ProjectViewSet

router = routers.DefaultRouter()
router.register('project', ProjectViewSet)
