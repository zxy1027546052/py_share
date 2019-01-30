# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-16 11:10'

from django.db import models



#访问网站的ip地址和次数
class Userip(models.Model):
    ip=models.CharField(verbose_name='IP地址',max_length=30)    #ip地址
    count=models.IntegerField(verbose_name='访问次数',default=0) #该ip访问次数
    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip
