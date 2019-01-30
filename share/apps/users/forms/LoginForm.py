# _*_ coding: utf-8 _*_
# 引入Django表单
from  django import forms

# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)