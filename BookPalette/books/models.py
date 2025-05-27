from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7)  # HEX 컬러코드
    cid_list = models.JSONField(null=True, blank=True)  # JSON 형태로 cid_list 저장
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    cover = models.URLField(max_length=300, blank=True, null=True)    
    summary = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True) 

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
    

class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
