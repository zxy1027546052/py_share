# _*_ coding: utf-8 _*_
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render

# 基于类实现需要继承的view
from django.urls import reverse
from django.views.generic.base import View

from users.forms import LoginForm

from users.models import Permission, UserProfile

from django.core import serializers


class LoginView(View):
    # 直接调用get方法免去判断
    def get(self, request):
        # render就是渲染html返回用户
        # render三变量: request 模板名称 一个字典写明传给前端的值
        redirect_url = request.GET.get('next', '')
        return render(request, "login.html", {
            "redirect_url": redirect_url
        })

    def post(self, request):
        # 类实例化需要一个字典参数dict:request.POST就是一个QueryDict所以直接传入
        # POST中的usernamepassword，会对应到form中
        login_form = LoginForm(request.POST)
        # 默认false
        request.session["is_login"] = False
        # is_valid判断我们字段是否有错执行我们原有逻辑，验证失败跳回login页面
        if login_form.is_valid():
            # 取不到时为空，username，password为前端页面name值
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            print("user_name", user_name, "pass_word", pass_word)
            # 成功返回user对象,失败返回null
            user = authenticate(username=user_name, password=pass_word)
            # print("user: ", user.is_active)
            print("user:", user)
            print(UserProfile.objects.filter(email=user_name))
            print("*" * 20)
            # 如果不是null说明验证成功
            if user is not None:
                # 只有当用户激活时才给登录
                # if user.is_active:
                if True:
                    # login_in 两参数：request, user
                    # 实际是对request写了一部分东西进去，然后在render的时候：
                    # request是要render回去的。这些信息也就随着返回浏览器。完成登录
                    login(request, user)
                    # 跳转到首页 user request会被带回到首页
                    # 存入session 序列化用户对象
                    user_dict = {}
                    user_ser = UserProfile.objects.filter(email=user_name)[0]
                    user_dict["is_admin"] = user_ser.is_admin
                    user_dict["user_name"] = user_ser.username
                    request.session["user"] = user_dict
                    request.session["is_login"] = True
                    # 增加重定向回原网页。
                    redirect_url = request.POST.get('next', '')

                    if redirect_url:
                        return HttpResponseRedirect(redirect_url)
                    # 跳转到首页 user request会被带回到首页
                    return HttpResponseRedirect(reverse("index"))
                # 即用户未激活跳转登录，提示未激活
                else:
                    return render(
                        request, "login.html", {
                            "msg": "用户名未激活! 请前往邮箱进行激活"})
            # 仅当用户真的密码出错时
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误!"})
        # 验证不成功跳回登录页面
        # 没有成功说明里面的值是None，并再次跳转回主页面
        else:
            return render(
                request, "login.html", {
                    "login_form": login_form})
