# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-08 12:46'
from .models import AddFileModel
from  django import forms

class AddfileForms(forms.Form):

#这里写的是前端页面里面的名称
    class Mate:
        model = AddFileModel
        fields = ['filename',
                  'filedepartment',
                  'filedes',
                  'fileusedfor',
                  'fileupload',
                  ]