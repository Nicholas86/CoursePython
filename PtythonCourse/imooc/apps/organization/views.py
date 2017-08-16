# -*- coding: utf-8 -*-
# from django.shortcuts import render

# Create your views here.
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 一.django框架


# 二.rest_framework框架
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route,list_route

# 三.本项目的model
from .models import *
from .serializers import *


# 1.城市列表
class CityDictModelViewSet(viewsets.ModelViewSet):
    queryset = CityDict.objects.all()
    serializer_class = CityDictSerializers

    @list_route(methods=['post',])
    def citylist(self,request,*args,**kwargs):
        city_arr = CityDict.objects.all()
        city_serializer = self.get_serializer(city_arr,many=True)
        jesonDic = {'list':city_serializer.data,'result': 'SUCCESS', 'errorMessage': '查询城市成功'}
        return Response(jesonDic)

# 2.机构
class CourseOrgModelViewSet(viewsets.ModelViewSet):
    queryset = CourseOrg.objects.all()
    serializer_class = CourseOrgSerializers

    @list_route(methods=['post', ])
    def courseOrlist(self, request, *args, **kwargs):
        if request.POST['id'] is not None:
            course_arr = CourseOrg.objects.filter(city__courseorg=request.POST['id'])
            course_serializer = self.get_serializer(course_arr, many=True)
            jesonDic = {'list': course_serializer.data, 'result': 'SUCCESS', 'errorMessage': '查询机构成功'}
            return Response(jesonDic)
        jesonDic = {'list':[], 'result': 'failue', 'errorMessage': '查询机构失败'}
        return Response(jesonDic)

# 3.添加机构点击数
class AddClickNumberModelViewSet(viewsets.ModelViewSet):
    queryset = CourseOrg.objects.all()
    serializer_class = CourseOrgSerializers

    @list_route(methods=['post', ])
    def addClickNumber(self, request, *args, **kwargs):
        if request.POST['id'] is not None:
            courseOrg = CourseOrg.objects.get(pk=request.POST['id'])
            courseOrg.click_nums += 1
            courseOrg.save()
            course_serializer = self.get_serializer(courseOrg,)
            jesonDic = {'list': course_serializer.data, 'result': 'SUCCESS', 'errorMessage': '点击成功'}
            return Response(jesonDic)
        jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '查询机构失败'}
        return Response(jesonDic)


# 4.添加收藏
def AddFavNums(id):
    courseOrg = CourseOrg.objects.get(pk=id)
    courseOrg.fav_nums += 1
    courseOrg.save()
    # return {'errorMessage': '收藏成功'}

# 5.取消收藏
def DeleteFavNums(id):
    courseOrg = CourseOrg.objects.get(pk=id)
    courseOrg.fav_nums -= 1
    courseOrg.save()
    # return {'errorMessage': '收藏成功'}

