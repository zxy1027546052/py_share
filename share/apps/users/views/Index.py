# _*_ coding: utf-8 _*_
from django.shortcuts import render

# 基于类实现需要继承的view
from django.views.generic.base import View

from sharefile.models import AddFileModel
from users.models import UserProfile
from utils.mixin_utils import LoginRequiredMixin



class Index(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self,request):
        # 从session获取用户信息
        user = request.session.get("user")
        user_name = user.get("user_name")
        # 查询对应用户信息
        user_obj = UserProfile.objects.filter(email=user_name)[0]
        # 部门id
        dep_id = user_obj.department_id
        # 查询部门对应的文件
        allfile = AddFileModel.objects.filter(department_id=dep_id)
        return render(request, 'Ace-dashboard-table-basic.html', {
                'allfile': allfile,
            })