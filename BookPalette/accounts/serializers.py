from rest_framework import serializers
from .models import User
from books.models import Category, Book, UserBookRelation
from community.models import Thread  # 필요하면!
from books.serializers import CategorySerializer, BookSerializer
# from community.serializers import ThreadSerializer

class UserRegisterSerializer(serializers.ModelSerializer):
    favorite_categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )
    class Meta:
        model = User
        fields = ('username', 'password', 'favorite_categories')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        favorite_categories = validated_data.pop('favorite_categories', [])
        user = User.objects.create_user(**validated_data)
        user.favorite_categories.set(favorite_categories)

        # (초기 색상 결정) 3개 카테고리 색상의 평균/논리로 결정
        colors = [cat.color for cat in favorite_categories if hasattr(cat, 'color')]
        if colors:
            user.profile_color = average_hex_color(colors)
            user.save()
        return user

def average_hex_color(hex_list):
    def hex_to_rgb(h): return tuple(int(h.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    def rgb_to_hex(r,g,b): return "#{:02x}{:02x}{:02x}".format(r,g,b)
    rgbs = [hex_to_rgb(h) for h in hex_list]
    avg = lambda i: int(sum(x[i] for x in rgbs) / len(rgbs))
    return rgb_to_hex(avg(0), avg(1), avg(2))

class UserSerializer(serializers.ModelSerializer):
    favorite_categories = CategorySerializer(many=True, read_only=True)
    # 좋아요한 책
    liked_books = serializers.SerializerMethodField()
    # 읽은 책
    read_books = serializers.SerializerMethodField()
    # 좋아요한 스레드(스레드 모델/시리얼라이저 구조에 따라)
    # liked_threads = serializers.SerializerMethodField() # community 구현시 추가

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'profile_color',
            'favorite_categories', 'liked_books', 'read_books', # 'liked_threads'
        ]
        read_only_fields = ['id', 'username', 'email']

    def get_liked_books(self, user):
        books = Book.objects.filter(userbookrelation__user=user, userbookrelation__status='like')
        return BookSerializer(books, many=True).data

    def get_read_books(self, user):
        books = Book.objects.filter(userbookrelation__user=user, userbookrelation__status='read')
        return BookSerializer(books, many=True).data

    # 아래 community가 구현되어 있다면 활성화
    # def get_liked_threads(self, user):
    #     threads = Thread.objects.filter(threadlike__user=user)
    #     return ThreadSerializer(threads, many=True).data
