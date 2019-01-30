# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-16 11:10'

from django.db import models



#网站总访问次数
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='网站访问总次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = u'网站访问总次数'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)