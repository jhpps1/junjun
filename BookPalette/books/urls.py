from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, BookViewSet, UserBookRelationViewSet,
    recommend_similar_books, popular_books
)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('relations', UserBookRelationViewSet)

urlpatterns = [
    path('books/popular/', popular_books),          # 커스텀 엔드포인트를 router include보다 먼저!
    path('books/recommend/', recommend_similar_books),
    path('', include(router.urls)),
]
