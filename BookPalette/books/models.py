from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7)  # HEX 컬러코드

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=7)  # 카테고리 color 복사 or 커스텀

    def save(self, *args, **kwargs):
        if not self.color:
            self.color = self.category.color
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserBookRelation(models.Model):
    STATUS_CHOICES = (
        ('read', '읽음'),
        ('like', '찜'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book', 'status')

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.get_status_display()})"
    
    
