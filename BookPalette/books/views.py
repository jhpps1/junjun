from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, Book, UserBookRelation
from .serializers import CategorySerializer, BookSerializer, UserBookRelationSerializer
from .utils import hex_to_rgb, color_distance
from accounts.models import User

# ===== 카테고리 목록 조회 =====
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ===== 도서 목록/상세/생성 등 =====
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

# ===== 유저-책 관계(찜/읽음 등) =====
class UserBookRelationViewSet(viewsets.ModelViewSet):
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        status = self.request.query_params.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs.filter(user=user)

# ===== 색상 기반 추천 API (가장 비슷/가장 다른 유저) =====
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_similar_books(request):
    user = request.user
    if not user.profile_color:
        return Response({"similar": [], "opposite": []})

    my_color = hex_to_rgb(user.profile_color)
    others = User.objects.exclude(id=user.id).exclude(profile_color__isnull=True)

    min_dist = float('inf')
    max_dist = -1
    similar_user = None
    opposite_user = None

    for u in others:
        try:
            u_color = hex_to_rgb(u.profile_color)
            dist = color_distance(my_color, u_color)
            if dist < min_dist:
                min_dist = dist
                similar_user = u
            if dist > max_dist:
                max_dist = dist
                opposite_user = u
        except Exception:
            continue

    data = {}

    # 가장 비슷한 색상 유저의 찜 책 추천
    if similar_user:
        like_ids = UserBookRelation.objects.filter(
            user=similar_user, status="like"
        ).values_list("book_id", flat=True)
        similar_books = Book.objects.filter(id__in=like_ids)[:10]
        data['similar'] = BookSerializer(similar_books, many=True).data
        data['similar_user'] = {
            "username": similar_user.username,
            "profile_color": similar_user.profile_color,
        }
    else:
        data['similar'] = []

    # 가장 다른 색상 유저의 찜 책 추천
    if opposite_user:
        like_ids = UserBookRelation.objects.filter(
            user=opposite_user, status="like"
        ).values_list("book_id", flat=True)
        opposite_books = Book.objects.filter(id__in=like_ids)[:10]
        data['opposite'] = BookSerializer(opposite_books, many=True).data
        data['opposite_user'] = {
            "username": opposite_user.username,
            "profile_color": opposite_user.profile_color,
        }
    else:
        data['opposite'] = []

    return Response(data)
