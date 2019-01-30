# from django.db import models
# from datetime import datetime
# from django.contrib.auth.models import AbstractUser
# Create your models here.

# # 部门
# class Department(models.Model):
#     Department = models.CharField(verbose_name=u"部门", max_length=20, default="All")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#
#     class Mate:
#         verbose_name = u"部门"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.Department
#
# # 用户Profile
# class UserProfile(AbstractUser):
#
#     # username = models.CharField(max_length=50, verbose_name=u"用户名")
#     # password = models.CharField(max_length=50, verbose_name=u"密码")
#
#     # 自定义的性别选择规则
#     GENDER_CHOICES = (
#         ("male", u"男"),
#         ("female", u"女")
#     )
#
#     department = models.ForeignKey(Department,on_delete=models.CASCADE)
#
#     # 昵称
#     nick_name = models.CharField(max_length=50, verbose_name=u"昵称")
#     # 生日，可以为空
#     birthday = models.DateField(verbose_name=u"生日", null=True, blank=True, default=None)
#
#
#     # 性别 只能男或女，默认女
#     gender = models.CharField(
#         max_length=6,
#         verbose_name=u"性别",
#         choices=GENDER_CHOICES,
#         default="female",)
#     # 地址
#     address = models.CharField(max_length=100, verbose_name="地址")
#     # 电话
#     mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
#     # 头像 默认使用default.png
#     image = models.ImageField(
#         upload_to="image/%Y/%m",
#         default=u"image/default.png",
#         max_length=100,
#         verbose_name=u"头像"
#     )
#
#     # meta信息，即后台栏目名
#     class Meta:
#         verbose_name = "用户信息"
#         verbose_name_plural = verbose_name
#
#     # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
#     def __str__(self):
#         return self.username
#
#     # # 获取用户未读消息的数量
#     # def unread_nums(self):
#     #     from operation.models import UserMessage
#     #     return  UserMessage.objects.filter(has_read=False, user=self.id).count()

# # 邮箱验证码model
# class EmailVerifyRecord(models.Model):
#     SEND_CHOICES = (
#         ("register", u"注册"),
#         ("forget", u"找回密码"),
#         ("update_email", u"修改邮箱"),
#     )
#     code = models.CharField(max_length=20, verbose_name=u"验证码")
#     # 未设置null = true blank = true 默认不可为空
#     email = models.EmailField(max_length=50, verbose_name=u"邮箱")
#     send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name=u"验证码类型")
#     # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
#     send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")
#
#     class Meta:
#         verbose_name = "邮箱验证码"
#         verbose_name_plural = verbose_name
#
#     # 重载str方法使后台不再直接显示object
#     def __str__(self):
#         return '{0}({1})'.format(self.code, self.email)


# class Role(models.Model):
#     role = models.ForeignKey(Department, on_delete=models.CASCADE)
#     name = models.CharField(max_length=32)
#     class Meta:
#         verbose_name_plural = '角色表'
#     def __str__(self):
#         return self.name
# #用户到角色分配
# class User2Role(models.Model):
#     u = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null = True)
#     r = models.ForeignKey(Role,on_delete=models.CASCADE,null = True)
#     class Meta:
#         verbose_name_plural = '用户分配角色'
#     def __str__(self):
#         return "%s-%s" %(self.u.username,self.r.name,)
# #添加权限
# class PermissionList(models.Model):
#     # get  获取用户信息1
#     # post  创建用户2
#     # delete 删除用户3
#     # put  修改用户4
#     name = models.CharField(max_length=32)
#     code = models.CharField(max_length=32)
#
#     class Meta:
#         verbose_name_plural = '操作表'
#     def __str__(self):
#         return self.name
#
# class Permission(models.Model):
#
#     user = models.ForeignKey(User2Role,on_delete=models.CASCADE,null = True) #这个里面一已经有用户和部门，和对应的职位
#     U2R = models.ForeignKey(PermissionList,on_delete=models.CASCADE,null = True)
#
#     class Meta:
#         verbose_name_plural = '权限'
#     def __str__(self):
#         return "%s-%s" %(self.user.u.username,self.U2R.name,)






