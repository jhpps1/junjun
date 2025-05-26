from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView, RegisterView, LogoutView  # ★ 추가/확인

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
urlpatterns += router.urls
