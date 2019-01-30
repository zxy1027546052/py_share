# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views import View

_author_ = 'Ace'
_date_ = '2019-01-27 21:55'

class WheelView(View):
    def get(self,request):
        return render(request,'Tools-wheel-widget-data.html')
