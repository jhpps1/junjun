from rest_framework import serializers
from .models import Category, Book, UserBookRelation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'color']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'category_id', 'color']

class UserBookRelationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book_detail = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UserBookRelation
        fields = ['id', 'user', 'book', 'status', 'created_at', 'book_detail']
        read_only_fields = ['id', 'created_at', 'book_detail']

    def get_book_detail(self, obj):
        return {
            "id": obj.book.id,
            "title": obj.book.title,
            "author": obj.book.author,
            "color": obj.book.color,
        }