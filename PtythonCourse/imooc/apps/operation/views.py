# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.shortcuts import render

# Create your views here.

# 一.django框架


# 二.rest_framework框架
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route,list_route

# 三.本项目的model
from .models import *
from .serializers import *

from organization.views import AddFavNums,DeleteFavNums

from courses.views import CourseAddFavNums,CourseDeleteFavNums,CourseAddStudy
from courses.models import Course
from courses.serializers import CourseSerializers
# 1.我要学习
class UserAskModelViewSet(viewsets.ModelViewSet):
    queryset = UserAsk.objects.all()
    serializer_class = UserAskSerializers

    @list_route(methods=['post',])
    def userAsk(self,request,*args,**kwargs):
        if request.POST['name'] is None:
            return Response({'list': [], 'result': 'failue', 'errorMessage': '用户名不能为空'})
        elif request.POST['mobile'] is None:
            return Response({'list': [], 'result': 'failue', 'errorMessage': '手机号不能为空'})
        elif request.POST['coursename'] is None:
            return Response({'list': [], 'result': 'failue', 'errorMessage': '课程名不能为空'})
        userAsk = UserAsk(name=request.POST['name'],mobile=request.POST['mobile'],
                           course_name=request.POST['coursename'])
        if userAsk:
            userAsk.save()
            userAsk_serializer = UserAskSerializers(userAsk)
            return Response({'list': userAsk_serializer.data, 'result': 'SUCCESS', 'errorMessage': '添加学习成功'})
        return Response({'list': [], 'result': 'failue', 'errorMessage': '添加学习失败'})


# 2.课程评论-添加
class AddCourseCommentsModelViewSet(viewsets.ModelViewSet):
    queryset = CourseComments.objects.all()
    serializer_class = CourseCommentsSerializers

    @list_route(methods=['post', ])
    def addCourseComments(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        comments = request.POST['comments']
        id = request.POST['id']
        if user_id is None:
            jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '该用户暂未登录'}
            return Response(jesonDic)
        if comments is None:
            jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '请填写评论内容'}
            return Response(jesonDic)
        if id is not None:
            course_comment = CourseComments()
            course_comment.user_id = user_id
            course_comment.comments = comments
            course_comment.course_id = id
            course_comment.save()
            course_serializer = self.get_serializer(course_comment)
            jesonDic = {'list': course_serializer.data, 'result': 'SUCCESS', 'errorMessage': '添加评论成功'}
            return Response(jesonDic)
        jesonDic = {'list':[], 'result': 'failue', 'errorMessage': '添加评论失败'}
        return Response(jesonDic)


# 3.收藏
class UserFavoriteModelViewSet(viewsets.ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializers

    @list_route(methods=['post',])
    def addUserFavorite(self,request,*args,**kwargs):
        # user = models.ForeignKey(UserProfile, verbose_name=u'用户')
        # # ID 是课程的 ID 或者是 讲师、课程机构的 ID
        # fav_id = models.IntegerField(default=0, verbose_name=u'收藏数据 Id')
        # fav_type = models.IntegerField(choices=((1, u'课程'),
        #                                         (2, u'课程机构'),
        #                                         (3, u'讲师')),
        user_id = request.POST['user_id']
        fav_type = request.POST['fav_type']
        fav_id = request.POST['id']
        if  user_id is not None and fav_type is not None:

            userFavorite_arr = UserFavorite.objects.filter(user_id=user_id,fav_type=fav_type,fav_id=fav_id)
            if userFavorite_arr:
                userFavorite_arr.delete()#删除收藏
                if fav_type == str(2):#1.课程 2.机构 3.讲师
                    DeleteFavNums(fav_id)
                elif fav_type == str(1):
                    CourseDeleteFavNums(fav_id)
                jesonDic = {'list': [], 'result': 'SUCCESS', 'errorMessage': '取消收藏成功'}
                return Response(jesonDic)

            userFavorite = UserFavorite(user_id=user_id,fav_id=fav_id,fav_type=fav_type)
            if userFavorite:
                userFavorite.save()
                if fav_type == str(2):#1.课程 2.机构 3.讲师
                    AddFavNums(fav_id)
                elif fav_type == str(1):
                    CourseAddFavNums(fav_id)
                userFavorite_serializer = self.get_serializer(userFavorite,)
                jesonDic = {'list': userFavorite_serializer.data, 'result': 'SUCCESS', 'errorMessage': '收藏成功'}
                return Response(jesonDic)
            jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '收藏失败'}
            return Response(jesonDic)

        jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '收藏失败'}
        return Response(jesonDic)


# 4.我要学习
class CourseStudyAddModelViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCoursStudyAddSerializers

    @list_route(methods=['post', ])
    def addStudyCourse(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        id = request.POST['id']
        if user_id is None:
            jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '该用户暂未登录'}
            return Response(jesonDic)
        if id is None:
            jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '请添加要学习的课程'}
            return Response(jesonDic)
        user_course = UserCourse()
        user_course.user_id = user_id
        user_course.course_id = id
        user_course.save()
        CourseAddStudy(id)#改变课程学习人数
        userCourseStudyAddSerializers = self.get_serializer(user_course)
        jesonDic = {'list': userCourseStudyAddSerializers.data, 'result': 'SUCCESS', 'errorMessage': '添加我要学习成功'}
        return Response(jesonDic)


# 5.我学习过的课程
class CourseStudyListModelViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCoursStudyAddSerializers

    @list_route(methods=['post', ])
    def studyCourseList(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        if user_id is None:
            jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '该用户暂未登录'}
            return Response(jesonDic)
        # 获取该用户学习过的所有课程的id,放进数组里[1, 2]
        user_courseId_list = [user_course.course_id for user_course in
                              UserCourse.objects.filter(user_id=user_id)]
        print user_courseId_list
        course_list = Course.objects.filter(id__in=user_courseId_list)
        course_serializers = CourseSerializers(course_list,many=True)
        jesonDic = {'list': course_serializers.data, 'result': 'SUCCESS', 'errorMessage': '获取学过的课程成功'}
        return Response(jesonDic)












