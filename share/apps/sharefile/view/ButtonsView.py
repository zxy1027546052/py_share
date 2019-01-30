# _*_ coding: utf-8 _*_
from django.shortcuts import render

_author_ = 'Ace'
_date_ = '2019-01-27 21:55'
from django.views.generic.base import View


class ButtonsView(View):
    def get(self,request):
        return render(request,'Tools-anybuttons-ui-buttons.html')