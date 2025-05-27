from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404 # 이거 내가 추가한거;; 뭐지...
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from books.models import Category
from .serializers import UserSerializer, UserRegisterSerializer
from django.contrib.auth import authenticate, login, logout, get_user_model

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer  # 회원가입용(비번 암호화)
        return UserSerializer  # 조회/수정용

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @action(detail=False, methods=['get', 'put'], url_path='me')
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 세션 인증일 경우
            return Response({'user': {'username': user.username, 'email': user.email}})
        else:
            return Response({'detail': '로그인 실패'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        favorite_categories = request.data.get('favorite_categories', [])  # [1,2,3]

        if not username or not password or len(favorite_categories) != 3:
            return Response({'detail': '필수 항목 누락 또는 카테고리 3개 선택해야 함'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'detail': '이미 존재하는 아이디입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        # 카테고리 ManyToMany 연결
        cats = Category.objects.filter(id__in=favorite_categories)
        user.favorite_categories.set(cats)

        # 초기 컬러값 계산 (간단 평균 예시)
        colors = [cat.color for cat in cats if hasattr(cat, "color")]
        if colors:
            user.profile_color = average_hex_color(colors)
            user.save()

        return Response({'user': {'username': user.username}})

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': '로그아웃 성공'})
    
def average_hex_color(hex_list):
    def hex_to_rgb(h): return tuple(int(h.lstrip("#")[i:i+2], 16) for i in (0,2,4))
    def rgb_to_hex(r,g,b): return "#{:02x}{:02x}{:02x}".format(r,g,b)
    rgbs = [hex_to_rgb(h) for h in hex_list]
    avg = lambda i: int(sum(x[i] for x in rgbs) / len(rgbs))
    return rgb_to_hex(avg(0), avg(1), avg(2))