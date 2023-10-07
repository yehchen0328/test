from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from.forms import RegisterForm
from.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import EnglishWord
from django.http import JsonResponse
from django.db.models import Q
'''from .email_utils import send_email_via_smtp'''
from django.core.mail import send_mail
import time
import random 

def otp():
    return ''.join(random.choices('0123456789', k=6))


@login_required(login_url="Login")
# Create your views here.
def index(request):
    return render(request,"home.html")
#註冊
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request,'register.html', context)
#登入
def sign_in(request):

    form = LoginForm()

    if request.method=="POST":
        username = request.POST.get("username")
        otp = request.POST.get("otp")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')

    context ={
        'form':form
    }

    return render(request,'login.html',context)

#登出
def log_out(request):

    logout(request)
    return redirect('Login')
'''
def some_view(request):
    
    send_email_via_smtp(user_email, password, to_email, subject, content)
'''
 #搜尋單字系統
def word_search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')  # 获取用户输入的查询词

        # 使用Q对象进行模糊搜索
        english_words = EnglishWord.objects.filter(Q(word__icontains=query) | Q(meaning__icontains=query))

        context = {
            'query': query,
            'english_words': english_words,
        }

        return render(request, 'search.html', context)
    
    return render(request, 'search.html')  # 渲染搜索页面

#登入畫面
def homepage(request):
    return render(request, 'hp.html')

def hp_slideshow(request):
    return render(request,'hp.html')

