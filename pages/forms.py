from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='이메일')
    phone_number = forms.CharField(max_length=15, required=False, label='전화번호')
    address = forms.CharField(widget=forms.Textarea, required=False, label='주소')
    bio = forms.CharField(widget=forms.Textarea, required=False, label='자기소개')
    
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput,
        help_text='비밀번호는 다음 조건을 만족해야 합니다:'
                 '• 8자 이상이어야 합니다.'
                 '• 숫자로만 이루어질 수 없습니다.'
                 '• 자주 사용되는 비밀번호는 사용할 수 없습니다.'
                 '• 개인정보와 비슷한 비밀번호는 사용할 수 없습니다.'
                 '• 비밀번호는 영문자, 숫자, 특수문자 조합으로 입력해주세요.'
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput,
        help_text='비밀번호를 다시 입력해주세요.'
    )
    username = forms.CharField(
        label='아이디',
        help_text='아이디는 15자 이하로 입력해주세요.<br>영문자, 숫자, @/./+/-/_ 만 사용 가능합니다.'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'address', 'bio')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            validate_password(password1, self.instance)
        except ValidationError as error:
            # 기본 영문 에러 메시지를 한글로 변환
            korean_errors = []
            for e in error:
                if 'too similar to' in str(e):
                    korean_errors.append('비밀번호가 개인정보와 너무 비슷합니다.')
                elif 'too common' in str(e):
                    korean_errors.append('너무 일반적인 비밀번호입니다.')
                elif 'entirely numeric' in str(e):
                    korean_errors.append('비밀번호는 숫자로만 이루어질 수 없습니다.')
                elif 'too short' in str(e):
                    korean_errors.append('비밀번호는 최소 8자 이상이어야 합니다.')
                else:
                    korean_errors.append(str(e))
            raise ValidationError(korean_errors)
        return password1

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 
                 'phone_number', 'address', 'profile_image', 'bio') 