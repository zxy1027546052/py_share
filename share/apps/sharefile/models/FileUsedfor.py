# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-16 11:09'

from _datetime import datetime
from django.db import models



# 用于
class FileUsedfor(models.Model):
    Usedfor = models.CharField(verbose_name=u"用于", max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Mate:
        verbose_name = u"用于"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.Usedfor