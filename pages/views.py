from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, '로그인되었습니다.')
            return redirect('pages:profile_edit')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    
    return render(request, 'pages/sign_in.html')

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('pages:profile_edit')
        else:
            messages.error(request, '입력하신 정보를 다시 확인해주세요.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'pages/sign_up.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 업데이트되었습니다.')
            return redirect('pages:profile_edit')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'pages/profile_edit.html', {'form': form})
