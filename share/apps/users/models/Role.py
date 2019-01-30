# _*_ coding: utf-8 _*_
from django.db import models

from users.models.Dep import Dep


_author_ = 'Ace'
_date_ = '2019-01-16 9:50'

# 2
class Role(models.Model):
    department_role = models.ForeignKey(Dep,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = u'角色表'
    def __str__(self):
        return "%s-%s" % (self.department_role.Department_name, self.name)