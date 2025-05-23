from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_color = models.CharField(max_length=7, default="#FFFFFF")  # HEX 컬러코드, 추후 업데이트 로직에서 활용
    # 필요시 추가 필드 여기에!
