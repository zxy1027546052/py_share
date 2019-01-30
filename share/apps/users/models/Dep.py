from datetime import datetime
from django.db import models


#定义部门
class Dep(models.Model):

    Department_name = models.CharField(verbose_name=u"部门", max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")


    class Meta:
        verbose_name_plural = u"部门"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.Department_name