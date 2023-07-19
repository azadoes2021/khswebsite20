from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    # email = forms.EmailField(
    #     error_messages={
    #         'required': '이메일을 입력해주세요.'
    #     },
    #     max_length=64, label='이메일'
    # )
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=64, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):        
        cleaned_data = super().clean()
        # email = cleaned_data.get('email')
        username = cleaned_data.get("username")
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')


        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else: 
                user = User(
                    username = username,
                    password = make_password(password)
                )
                user.save()    
                
class LoginForm(forms.Form):
    # email = forms.EmailField(
    #     error_messages={
    #         'required': '이메일을 입력해주세요.'
    #     },
    #     max_length=64, label='이메일'
    # )
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=64, label='아이디'
    )


    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):        
        cleaned_data = super().clean()
        # email = cleaned_data.get('email')
        username = cleaned_data.get("username")
        password = cleaned_data.get('password')
        
        #user.DoesNotExist를 User.DoesNotExist로 변경하여 에러처리 => 올바르게 작동
        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')
                return
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.username = user.username

            
            
            
            
            
            
            
            
            
            
            














