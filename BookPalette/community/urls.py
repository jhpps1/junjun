from rest_framework.routers import DefaultRouter
from .views import ThreadViewSet

router = DefaultRouter()
router.register('threads', ThreadViewSet)

urlpatterns = router.urls
