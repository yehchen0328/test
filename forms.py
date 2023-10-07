from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    otp = forms.CharField(
        label="一次性驗證碼",
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):

    username=forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    password=forms.CharField(
        label="密碼", 
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

class EmailOTPForm(forms.Form):

    email = forms.EmailField(label='Enter your email', max_length=150)