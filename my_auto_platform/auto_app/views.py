# 认证页面
from django.contrib.auth import authenticate, login
# 对应数据库
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# 创建表单
# from django import forms
# from auto_app.models import User
# class UserForm(forms.Form):
#     username=forms.CharField(label='用户名：',max_length=100)
#     password=forms.CharField(label='密码：',widget=forms.PasswordInput())
#     email=forms.EmailField(label='电子邮件：')

# Create your views here.
#登录
def my_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            ret = redirect('/shouye/') # 重定向首页
            return ret
        else:
            # 结合末班，返回一个渲染后的HttpResponse对象
            return render(request, '../templates/page/login.html', {"error_msg": "用户名或密码错误！"})
    else:
        return render(request, '../templates/page/login.html', {})

# def register(request):
#     if request.method=='POST':
#         uf=UserForm(request.POST)
#         if uf.is_valid():
#             #获取表单信息
#             username=uf.cleaned_data['username']
#             password=uf.cleaned_data['password']
#             email=uf.cleaned_data['email']
#             #将表单写入数据库
#             user=User()
#             user.username=username
#             user.password=password
#             user.email=email
#             user.save()
#
#             return render_to_response('success.html',{'username':username})
#     else:
#         uf=UserForm()
#         return render_to_response('register.html',{'uf':uf})


