# _*_ coding: utf-8 _*_
from django.shortcuts import render

from sharefile.forms import AddfileForms
from sharefile.models import AddFileModel
from sharefile.models.FileUsedfor import FileUsedfor
from users.models.Dep import Dep
from utils.mixin_utils import LoginRequiredMixin
from django.views.generic.base import View


class AddfileView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self,request):
        dept = Dep.objects.all()
        usedfor = FileUsedfor.objects.all()

        return render(request,'Ace-file-add-realestate-add-property.html',{
            'dept':dept,
            'usedfor': usedfor,
        })

    def post(self,request):
        addfile_form = AddfileForms(request.POST)

        file_profile = AddFileModel()

        if addfile_form.is_valid():
            file_profile.models_Filename = request.POST.get("filename", "")
            file_profile.models_Filedepartment = request.POST.get("filedepartment", "")
            file_profile.models_Filedes = request.POST.get("filedes", "")
            file_profile.models_Fileusedfor = request.POST.get("fileusedfor", "")


            if 'fileupload' in list(request.FILES.keys()):
                file_profile.models_Fileupload = request.FILES['fileupload']


            file_profile.models_Updated_date = datetime.now()
            # 保存
            file_profile.save()

            return redirect('/sharefile/filelist/')

        else:
            return render(request, 'Ace-file-add-realestate-add-property.html')