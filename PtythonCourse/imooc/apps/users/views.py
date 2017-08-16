# -*- coding: utf-8 -*-
# from django.shortcuts import render

# 一.django框架
from django.contrib.auth.hashers import make_password,check_password#密码加密

# 二.rest_framework框架
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route,list_route

# 三.本项目的model
from .models import *
from .serializers import *


# 1.注册
class RegisterModelViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    @list_route(methods=['post',])
    def register(self,request,*args,**kwargs):
        mobile = request.data['mobile']
        password = request.data['password']
        if self.queryset.filter(mobile__exact=mobile):
            jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '该账号已被注册'}
            return Response(jesonDic)
        if mobile is not None and password is not None:
            # 密码加密
            userProfile= UserProfile(mobile=mobile,password=make_password(password,None, 'pbkdf2_sha256'))
            userProfile.save()
            jesonDic = {'list':[],'result': 'SUCCESS', 'errorMessage': '注册成功'}
            return Response(jesonDic)
        jesonDic = {'list': [], 'result': 'failue', 'errorMessage': '注册失败'}
        return Response(jesonDic)


# 2.登录
class LoginModelViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    @list_route(methods=['post'],)
    def login(self,request,*args,**kwargs):
        register_arr = self.queryset.filter(mobile__exact=request.data['mobile'])
        if register_arr is None:
            return Response({'list': [], 'result': 'failue', 'errorMessage': '该账号没有注册,请先注册'})
        # 解密,验证明文密文
        if check_password(request.data['password'],register_arr.first().password) == False:
            return Response({'list': [], 'result': 'failue', 'errorMessage': '密码错误'})
        register_serializer = self.get_serializer(register_arr, many=True)
        return Response({'list': register_serializer.data, 'result': 'SUCCESS', 'errorMessage': '登录成功'})

# 3.更新个人信息
class UpdateUserInfoModelViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    @list_route(methods=['post',])
    def updateUserInfo(self,request,*args,**kwargs):
        print (request.data)

        user_id = request.data['userId']
        user_name = request.data['name']
        address = request.data['address']
        image = request.data['userImage']#图像key,跟iOS保持一致
        user_arr = self.queryset.get(id=user_id)
        user_arr.username = user_name
        user_arr.address = address
        user_arr.image = image
        user_arr.save()
        user_serializer = self.get_serializer(user_arr)
        return Response({'list': user_serializer.data, 'result': 'SUCCESS', 'errorMessage': '更新个人资料成功'})
















