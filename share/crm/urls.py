"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
# 用于设定图片URL地址
from django.views.static import serve

import xadmin
# 配件添加图片URL时用到的
from apps.users.views.ActiveUserView import ActiveUserView
from apps.users.views.ForgetPwdView import ForgetPwdView
from apps.users.views.Index import Index
from apps.users.views.LoginView import LoginView
from apps.users.views.LogoutView import LogoutView
from apps.users.views.ModifyPwdView import ModifyPwdView
from apps.users.views.RegisterView import RegisterView
from apps.users.views.ResetView import ResetView
from .settings import MEDIA_ROOT

# from users.views import user_login,LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView,LogoutView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^$', Index.as_view(), name="index"),
    # 基于类方法实现登录,这里是调用它的方法
    # path('', LoginView.as_view(), name="login"),
    # path('index/',TemplateView.as_view(''),name="index"),
    path('index/', Index.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    # 验证码url
    path("captcha/", include('captcha.urls')),
    # 激活用户url
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),

    # 忘记密码
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    # 重置密码urlc ：用来接收来自邮箱的重置链接, 用于在邮箱里面点击后，所要跳转到的页面链接
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),
    # 修改密码url; 用于passwordreset页面提交表单, 用于点击来链接里面提交密码。
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    # sharefile的URL
    path("sharefile/", include('sharefile.urls', namespace='sharefile')),

    # users的URL
    path("users/", include('users.urls', namespace='users')),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT， 其中document_root是一个固定写法。
    re_path('media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    path('logout/', LogoutView.as_view(), name='logout'),

    # path('profile/',ProfileView.as_view(),name='profile'),

]
