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

# 1.课程
class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    @list_route(methods=['post',])
    def courselist(self,request,*args,**kwargs):
        course_list = Course.objects.all()
        course_serializer = self.get_serializer(course_list,many=True)
        return Response({'list': course_serializer.data, 'result': 'SUCCESS', 'errorMessage': '获取课程列表成功'})

# 3.添加课程点击数
class AddCourseClickNumberModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    @list_route(methods=['post', ])
    def addClickNumber(self, request, *args, **kwargs):
        if request.POST['id'] is not None:
            courseOrg = Course.objects.get(pk=request.POST['id'])
            courseOrg.click_nums += 1
            courseOrg.save()
            course_serializer = self.get_serializer(courseOrg, )
            jesonDic = {'list': course_serializer.data, 'result': 'SUCCESS', 'errorMessage': '点击成功'}
            return Response(jesonDic)
        jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '增加点击失败'}
        return Response(jesonDic)


# 4.章节
class LessonModelViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    @list_route(methods=['post',])
    def lessonList(self,request,*args,**kwargs):
        if request.POST['id'] is not None:
            lesson_list = Lesson.objects.filter(course_id=request.POST['id'])
            lesson_serializer = self.get_serializer(lesson_list, many=True)
            # lesson_serializer = LessonSerializers(lesson_list)
            return Response({'list': lesson_serializer.data, 'result': 'SUCCESS', 'errorMessage': '获取章节列表成功'})
        jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '获取章节列表失败'}
        return Response(jesonDic)



#7 .添加收藏
def CourseAddFavNums(id):
    courseOrg = Course.objects.get(pk=id)
    courseOrg.fav_nums += 1
    courseOrg.save()
    # return {'errorMessage': '收藏成功'}

# 8.取消收藏
def CourseDeleteFavNums(id):
    courseOrg = Course.objects.get(pk=id)
    courseOrg.fav_nums -= 1
    courseOrg.save()
    # return {'errorMessage': '收藏成功'}

# 9.我要学习
def CourseAddStudy(id):
    courseOrg = Course.objects.get(pk=id)
    courseOrg.students += 1
    courseOrg.save()


