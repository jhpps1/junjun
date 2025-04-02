from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserChangeForm

# Create your views here.

def sign_in(request):
    return render(request, 'pages/sign_in.html')

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
