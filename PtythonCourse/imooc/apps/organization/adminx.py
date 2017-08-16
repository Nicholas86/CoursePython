#_*_encoding:utf-8_*_
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_per_page = 10  # 列表分页
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city__name', 'add_time']
    list_per_page = 10  # 列表分页
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面


class TeacherAdmin(object):
    list_display = ['name','org','work_years','work_company','work_position',
                    'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name','org', 'work_years','work_company',
                     'work_position','points','click_nums', 'fav_nums']
    list_filter = ['name','org__name','work_years','work_company',
                   'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    list_per_page = 10  # 列表分页
    refresh_times = (200, 3600)  # 5-10s刷新Goods页面

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
