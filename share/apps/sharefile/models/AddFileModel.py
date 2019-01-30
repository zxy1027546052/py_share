# _*_ coding: utf-8 _*_


_author_ = 'Ace'
_date_ = '2019-01-16 11:09'

from datetime import datetime
from django.urls import reverse



from users.models.Dep import Dep
from django.db import models



class AddFileModel(models.Model):

    models_Filename = models.CharField(max_length=20, verbose_name=u"文件名称", default='')
    models_Filedepartment = models.CharField(max_length=20, verbose_name=u"BUH", default='')
    # models_Filedepartment = models.ForeignKey(FileDepartment,on_delete=models.CASCADE,verbose_name=u"人数", default='')
    models_Filedes = models.TextField(verbose_name=u"描述", default='')

    models_Fileusedfor = models.CharField(max_length=20, verbose_name=u"人数", default='')
    # models_Fileusedfor = models.ForeignKey(FileUsedfor,on_delete=models.CASCADE,verbose_name=u"人数", default='')
    models_Fileupload = models.FileField(
        upload_to="file/%Y/%m",
        verbose_name=u"文件",
        max_length=1000, )
    models_Updated_date = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    models_clicknum = models.IntegerField(default=0, verbose_name=u"下载次数")
    #部门外键
    department = models.ForeignKey(Dep, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = u"上传文件"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[str(self.id)])

    def viewed(self):
        self.models_clicknum += 1
        self.save(update_fields=['models_clicknum'])