# _*_ coding: utf-8 _*_
from django.shortcuts import render

from sharefile.models.AddFileModel import AddFileModel

_author_ = 'Ace'
_date_ = '2019-01-27 21:54'
from django.views.generic.base import View


class CountDownloadView(View):
    def get(self,request,file_id):
        count = AddFileModel.objects()
        countfile = AddFileModel.objects.get(id=int(file_id))
        countfile.models_clicknum += 1
        countfile.save()
        return render(request,'Ace-filelist-transaction-listing.html',{
            'count':count,
        })