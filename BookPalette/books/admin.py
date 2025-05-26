from django.contrib import admin
from .models import Category, Book, UserBookRelation, BookComment

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(UserBookRelation)
admin.site.register(BookComment)
