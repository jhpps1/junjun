from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # 여기에 URL 패턴을 추가하세요
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
