from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BookViewSet, UserBookRelationViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('relations', UserBookRelationViewSet)

urlpatterns = router.urls
