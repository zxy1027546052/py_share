# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-16 11:10'

from django.utils import timezone
from django.db import models




#单日访问量统计
class DayNumber(models.Model):
    day=models.DateField(verbose_name='日期',default=timezone.now)
    count=models.IntegerField(verbose_name='网站访问次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = u'网站日访问量统计'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)

