#_*_encoding:utf-8_*_
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile


# ----- adminx 全局配置
class BaseSetting(views.BaseAdminView):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(views.CommAdminView):
    site_title = u'慕学后台管理系统'
    site_footer = u'慕学在线网'
    menu_style = 'accordion'
# ------


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']




# class UserProfileAdmin(object):
#     list_display = ['nick_name', 'birthday', 'address', 'mobile', 'image']
#     search_fields = ['title', 'image', 'url', 'index']
#     list_filter = ['nick_name', 'birthday', 'address', 'mobile', 'image']


# 卸载 django 自带的 auth_user
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)


# 继承自定义的 UserProfile 覆盖 django 自带的 auth_user
# xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
