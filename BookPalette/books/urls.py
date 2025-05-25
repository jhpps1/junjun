from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, BookViewSet, UserBookRelationViewSet,
    recommend_similar_books
)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('relations', UserBookRelationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/recommend/', recommend_similar_books),
]
