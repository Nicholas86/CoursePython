#_*_encoding:utf-8_*_

# from __future__ import unicode_literals

# 系统的类
from datetime import datetime


# django的类
from django.db import models

# 第三方类
# from organization.models import CourseOrg, Teacher
from django.conf import settings
ORGANIZATION_TEACHER_MODEL = getattr(settings, 'ORGANIZATION_TEACHER_MODEL', 'organization.Teacher')#用户
ORGANIZATION_COURSEORG_MODEL = getattr(settings, 'ORGANIZATION_COURSEORG_MODEL', 'organization.CourseOrg')#商品

# Create your models here.
class Course(models.Model):
    course_org = models.ForeignKey(ORGANIZATION_COURSEORG_MODEL, verbose_name=u'课程机构', null=True, blank=True)
    name = models.CharField(max_length=52, verbose_name=u'课程名字')
    desc =  models.CharField(max_length=300, verbose_name=u'课程描述')
    teacher = models.ForeignKey(ORGANIZATION_TEACHER_MODEL, verbose_name=u'讲师', null=True, blank=True)
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')),
                              max_length=2, verbose_name=u'难度')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否是轮播图')
    category = models.CharField(default=u'后端', max_length=20, verbose_name=u'课程类别')
    tag = models.CharField(default='', verbose_name=u'课程标签', max_length=10)
    youneed_konw = models.CharField(default='', max_length=300, verbose_name=u'课前须知')
    teacher_tell = models.CharField(default='', max_length=300, verbose_name=u'老师告诉你能学什么')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):#获取章节数量
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):#课程资源
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = u'轮播课程'
        verbose_name_plural = verbose_name
        # 如果不设置 proxy ，就会再生成一个 BannerCourse 数据表
        proxy = True


# 章节信息
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='videos',verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    url = models.URLField(max_length=200, verbose_name=u'访问地址', default='www.baidu.com')
    learn_times = models.IntegerField(default=0, verbose_name=u'视频时长(分钟数)')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'课件名')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name=u'资源文件', max_length=100)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
