from django import forms
from .models import User
from argon2 import PasswordHasher #비밀번호 암호화에 필요

class RegisterForm(forms.ModelForm):
    user_id = forms.CharField(
        label = '아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요.'}
    )

    user_pw = forms.CharField(
        label = '비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    user_pw_confirm = forms.CharField(
        label = '비밀번호 확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw-confirm',
                'placeholder' : '비밀번호 확인'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )

    user_name = forms.CharField(
        label = '이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-name',
                'placeholder' : '이름'
            }
        ),
        error_messages={'required' : '이름을 입력해주세요.'}
    )   

    field_order = [
            'user_id',
            'user_pw',
            'user_pw_confirm',
            'user_name',
        ]

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pw = cleaned_data.get('user_pw','')
        user_pw_confirm = cleaned_data.get('user_pw_confirm','')
        user_name = cleaned_data.get('user_name','')

    class Meta:
        model = User
        fields = [
            'user_id',
            'user_pw',
            'user_name',
        ]