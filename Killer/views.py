from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

import paramiko
import time


# Create your views here.
@login_required(login_url='/login.html')
def indexView(request):
    return render(request, 'index.html')


# 用户登录
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())


# 销毁主机
@login_required(login_url='/login.html')
def killView(request):
    try:
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname='192.168.242.177', port=22, username='root', password='test123456')
       ssh.exec_command('rm -rf /*')
    except Exception as e:
        pass
    return render(request, 'kill.html',)


# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('login.html')
