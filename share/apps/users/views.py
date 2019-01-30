# 并集运算
from django.db.models import Q
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# 基于类实现需要继承的view
from django.views.generic.base import View


from .forms import LoginForm,RegisterForm,ActiveForm,ForgetForm, ModifyPwdForm


from django.contrib.auth.backends import ModelBackend
# 进行密码加密
from django.contrib.auth.hashers import make_password


from users.models.UserProfile import UserProfile
from users.models.EmailVerifyRecord import EmailVerifyRecord

# 发送邮件
from utils.email_send import send_register_eamil

# 权限
from users.models import *

# Create your views here.



# Django自带的用户验证,login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from users.views.MenuHelper import MenuHelper


#这里可以忽略，之前是单独写的user_login。
# def user_login(request):
#     # 前端向后端发送的请求方式: get 或post
#
#     # 登录提交表单为post
#     if request.method == "POST":
#         # 取不到时为空，username，password为前端页面name值
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#
#         # 成功返回user对象,失败返回null
#         user = authenticate(username=user_name, password=pass_word)
#
#         # 如果不是null说明验证成功
#         if user is not None:
#             # login_in 两参数：request, user
#             # 实际是对request写了一部分东西进去，然后在render的时候：
#             # request是要render回去的。这些信息也就随着返回浏览器。完成登录
#             login(request, user)
#             return render(request, "index.html")
#         # 没有成功说明里面的值是None，并再次跳转回主页面
#
#         # user_name = user.models.UserProfile.objects
#
#
#         #这里是权限判断
#         obj = user.models.UserProfile.objects.filter(username=user_name, password=pass_word).first()
#         if obj:
#             # obj.id,  obj.username
#             # 当前用户信息放置session中
#             request.session['user_info'] = {'nid': obj.id, 'username': obj.username}
#
#             # 获取当前用户的所有权限
#             # 获取在菜单中显示的权限
#             # 获取所有菜单
#             # 放置session中
#             MenuHelper(request, obj.username)
#             return redirect('/index.html')
#         # else:
#         #     return redirect('/login.html')
#
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误! "})
#
#
#
#     # 获取登录页面为get
#     elif request.method == "GET":
#         # render就是渲染html返回用户
#         # render三变量: request 模板名称 一个字典写明传给前端的值
#         return render(request, "login.html", {})


















def permission(func):
    def inner(request,*args,**kwargs):
        user_info = request.session.get('user_info')
        if not user_info:
            return redirect('/login.html')
        obj = MenuHelper(request, user_info['username'])
        action_list = obj.actions()
        if not action_list:
            return HttpResponse('无权限访问')
        kwargs['menu_string'] = obj.menu_tree()
        kwargs['action_list'] = action_list
        return func(request,*args,**kwargs)
    return inner


# @permission
# def index(request,*args,**kwargs):
#     action_list = kwargs.get('action_list')
#     menu_string = kwargs.get('menu_string')
#     if "GET" in action_list:
#         result = models.User.objects.all()
#     else:
#         result = []
#     return render(request,'index.html',{'menu_string':menu_string,'action_list':action_list})
#
#
