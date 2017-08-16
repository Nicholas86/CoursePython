# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 1.django
from django.conf.urls import url,include

# 2.api文件
from .views import *

# 3.rest_framewor框架
from rest_framework import routers

# 4.organization,courses,users,operation模块
import organization
from organization import views

import courses
from courses import views

import users
from users import views

import operation
from operation import views

# 初始化路由对象
router = routers.DefaultRouter()
router.register(r'users_register',users.views.RegisterModelViewSet)#1.注册
router.register(r'users_login',users.views.LoginModelViewSet)#2.登录
router.register(r'org_city_list',organization.views.CityDictModelViewSet)#3.城市列表
router.register(r'org_courseOrg_list',organization.views.CourseOrgModelViewSet)#4.机构组织
router.register(r'org_courseOrg_addClickNumber',organization.views.AddClickNumberModelViewSet)#5.组织点击数
router.register(r'operation_userAsk_add',operation.views.UserAskModelViewSet)#6.我要学习
router.register(r'operation_userFavorite_add',operation.views.UserFavoriteModelViewSet)#7.收藏
router.register(r'operation_courseComments_add',operation.views.AddCourseCommentsModelViewSet)#8.添加评论
router.register(r'courses_course_list',courses.views.CourseModelViewSet)#9.课程列表
router.register(r'courses_course_addClickNumber',courses.views.AddCourseClickNumberModelViewSet)#10.课程增加点击
router.register(r'courses_lesson_list',courses.views.LessonModelViewSet)#11.章节列表
router.register(r'operation_study_add',operation.views.CourseStudyAddModelViewSet)#12.我要学习
router.register(r'operation_study_list',operation.views.CourseStudyListModelViewSet)#13.我学习过的课程
router.register(r'users_info_update',users.views.UpdateUserInfoModelViewSet)#14.更新个人资料

urlpatterns = [
    url(r'^', include(router.urls)),  # 路由api
]










