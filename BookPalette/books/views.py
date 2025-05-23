from rest_framework import viewsets, filters, permissions
from .models import Category, Book, UserBookRelation
from .serializers import CategorySerializer, BookSerializer, UserBookRelationSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    # 추가로 category filtering도 지원
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class UserBookRelationViewSet(viewsets.ModelViewSet):
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 내 기록만 필터링
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        status = self.request.query_params.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs.filter(user=user)