# _*_ coding: utf-8 _*_
from django.db import models

from users.models import Dep
from users.models.UserProfile import UserProfile
from users.models.Role import Role

_author_ = 'Ace'
_date_ = '2019-01-16 9:55'

#3用户到角色分配
class User2Role(models.Model):
    u = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    r = models.ForeignKey(Role,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = '用户分配角色'
    def __str__(self):
        return "%s:%s-%s" %(self.r.department_role.Department_name,self.u.username,self.r.name)