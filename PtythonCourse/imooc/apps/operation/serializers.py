# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 我们会在api目录中构建所有的API功能
from rest_framework import serializers

# 本项目model
from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse

# 1.我要学习
class UserAskSerializers(serializers.ModelSerializer):
    # Meta类允许你去指定模型序列化以及给序列化包含的字段。
    # 所有的模型字段都会被包含如果你没有设置一个fields属性。
    class Meta:
        model = UserAsk
        fields = '__all__'


# 2.课程评论
class CourseCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseComments
        fields = '__all__'


# 3.收藏
class UserFavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = '__all__'


# 4.我要学习
class UserCoursStudyAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'


