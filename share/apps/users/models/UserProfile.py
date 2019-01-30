# _*_ coding: utf-8 _*_
from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.models import AbstractUser
from django.db import models

# 用户Profile
from users.models.Dep import Dep


class UserProfile(AbstractUser):
    # username = models.CharField(max_length=50, verbose_name=u"用户名")
    # password = models.CharField(max_length=50, verbose_name=u"密码")
    # user_email = models.CharField(max_length=50, verbose_name=u"邮箱")

    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

    # department = models.ForeignKey(Department,on_delete=models.CASCADE,default=None)

    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称")
    # 生日，可以为空
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True, default=None)

    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=6,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female", )
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100,
        verbose_name=u"头像"
    )

    # 部门外键
    department = models.ForeignKey(Dep, on_delete=models.CASCADE, null=True)
    # 是否有权限 0 没有 1 有
    is_admin = models.BooleanField(null=False, default=False)

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
    def __str__(self):
        return self.username

    # # 获取用户未读消息的数量
    # def unread_nums(self):
    #     from operation.models import UserMessage
    #     return  UserMessage.objects.filter(has_read=False, user=self.id).count()
