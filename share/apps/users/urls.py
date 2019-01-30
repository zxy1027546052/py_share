# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-28 14:05'
from django.urls import path, include, re_path
from users.views.ProfileView import ProfileView

app_name = 'users'


urlpatterns = [
        path('profile/', ProfileView.as_view(), name='profile'),
        ]