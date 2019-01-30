# _*_ coding: utf-8 _*_
from users.models import Role, Permission, User2Role, PermissionList
from users.models.Dep import Dep

_author_ = 'Ace'
_date_ = '2018/11/29 12:40'

from users.models.EmailVerifyRecord import EmailVerifyRecord
from users.models.UserProfile import UserProfile
#from .models import Users,Role,Action,Permission,Users2Role,Permission2Action,Permission2Action2Role
from . import models
import xadmin
# 和X admin的view绑定
from xadmin import views

# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True



# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['code', 'email','send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "学校文件上传系统"
    site_footer = "Created by Ace"
    # 收起菜单
    # menu_style = "accordion"


# 将model与admin管理器进行关联注册

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

#将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)
#
#将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)


# class UserProfileAdmin(object):
#     # 配置后台我们需要显示的列
#     list_display = [
#                     'username',
#                     'password',
#                     'user_email',
#                     'GENDER_CHOICES',
#                     'nick_name',
#                     'birthday',
#                     'gender',
#                     'address',
#                     'mobile',
#                     'image',
#                     ]
#     # 配置搜索字段,不做时间搜索
#     search_fields = [
#                     'username',
#                     'password',
#                     'user_email',
#                     'GENDER_CHOICES',
#                     'nick_name',
#                     'birthday',
#                     'gender',
#                     'address',
#                     'mobile',
#                     'image',
#                     ]
#     # 配置筛选字段
#     list_filter = [
#                     'username',
#                     'password',
#                     'user_email',
#                     'GENDER_CHOICES',
#                     'nick_name',
#                     'birthday',
#                     'gender',
#                     'address',
#                     'mobile',
#                     'image',
#                     ]
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)


#创建权限列表
#注册权限
# xadmin.site.register(models.Role)


# 添加权限

# class DepartmentAdmin(object):
#     # 配置后台我们需要显示的列
#     list_display = ['user','Department_name']
#     # 配置搜索字段,不做时间搜索
#     search_fields = ['user','Department_name']
#     # 配置筛选字段
#     list_filter = ['user','Department_name']
# xadmin.site.register(Department,DepartmentAdmin)


class DepAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['Department_name','add_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['Department_name','add_time']
    # 配置筛选字段
    list_filter = ['Department_name','add_time']
xadmin.site.register(Dep,DepAdmin)

#注册权限
class RoleAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['department_role','name']
    # 配置搜索字段,不做时间搜索
    search_fields = ['department_role','name']
    # 配置筛选字段
    list_filter = ['department_role','name']
xadmin.site.register(Role,RoleAdmin)

#注册用户到角色分配
class PermissionAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['user','U2R']
    # 配置搜索字段,不做时间搜索
    search_fields = ['user','U2R']
    # 配置筛选字段
    list_filter = ['user','U2R']
xadmin.site.register(Permission,PermissionAdmin)



#User2Role
class User2RoleAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['u','r']
    # 配置搜索字段,不做时间搜索
    search_fields = ['u','r']
    # 配置筛选字段
    list_filter = ['u','r']
xadmin.site.register(User2Role,User2RoleAdmin)


#注册添加权限
class PermissionListAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['name','code']
    # 配置搜索字段,不做时间搜索
    search_fields = ['name','code']
    # 配置筛选字段
    list_filter = ['name','code']
xadmin.site.register(PermissionList,PermissionListAdmin)




