# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-16 9:58'

from django.db import models
from users.models.PermissionList import PermissionList
from users.models.User2Role import User2Role


# 5
class Permission(models.Model):

    user = models.ForeignKey(User2Role,on_delete=models.CASCADE) #这个里面一已经有用户和部门，和对应的职位
    U2R = models.ForeignKey(PermissionList,on_delete=models.CASCADE) #null = True

    class Meta:
        verbose_name_plural = '权限'
    def __str__(self):
        return "%s-%s-%s" %(self.user.r.department_role.Department_name,self.user.u.username,self.U2R.name,)