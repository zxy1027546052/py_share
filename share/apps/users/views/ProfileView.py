# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect
from django.views.generic.base import View

from utils.mixin_utils import LoginRequiredMixin

_author_ = 'Ace'
_date_ = '2019-01-28 13:57'

class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'Ace-pages-profile.html')
