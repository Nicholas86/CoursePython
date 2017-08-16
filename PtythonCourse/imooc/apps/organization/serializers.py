# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 我们会在api目录中构建所有的API功能
from rest_framework import serializers

# 本项目model
from .models import CityDict,CourseOrg,Teacher

# 1.城市
class CityDictSerializers(serializers.ModelSerializer):
    # Meta类允许你去指定模型序列化以及给序列化包含的字段。
    # 所有的模型字段都会被包含如果你没有设置一个fields属性。
    class Meta:
        model = CityDict
        fields = '__all__'

# 2.机构
class CourseOrgSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseOrg
        fields = '__all__'
