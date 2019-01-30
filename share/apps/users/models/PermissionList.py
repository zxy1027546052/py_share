# _*_ coding: utf-8 _*_
from django.db import models

_author_ = 'Ace'
_date_ = '2019-01-16 9:58'

#3添加权限
class PermissionList(models.Model):
    # get  获取用户信息1
    # post  创建用户2
    # delete 删除用户3
    # put  修改用户4
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '操作表'
    def __str__(self):
        return "%s-%s" % (self.name, self.code)
