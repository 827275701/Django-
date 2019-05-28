from django.conf.urls import url, include

from . import views

urlpatterns = [
    #普通用户
    url('login', views.android_login),  #yes
    url('choose_spot', views.android_choose_spot),  #yes
    url('now_data', views.android_now_data),  #yes
    url('person_info', views.android_person_info),  #yes
    url('history_day', views.android_history_day),  #yes
    url('history_week', views.android_history_week),
    url('history_month', views.android_history_month),
    url('history_year', views.android_history_year),
    url('change_password', views.android_change_password),

    #admin
    url('admin', views.admin_index),  #yes

    #用户相关
    url('add_user', views.android_add_user),  #yes
    url('delete_user', views.android_delete_user),
    url('select_user', views.android_select_user),
    url('get_person', views.android_get_person),
    url('change_other_info', views.android_change_other_info),

    url('change_other_password', views.android_admin_change_other_password),
    url('change_other_name', views.android_admin_change_other_name),
    url('change_other_no', views.android_admin_change_other_no),
    url('change_other_sex', views.android_admin_change_other_sex),

    #博览室相关
    #url('get_room', views.android_get_room),#获得当前已存在博览室的 名称和ID
    url('select', views.android_select_room),  # 获得当前已存在博览室的 名称和ID和位置
    url('change_room_info', views.android_change_room_info),  # 获得当前已存在博览室的 名称和ID和位置
    url('get_the_room_info', views.android_get_the_room_info),

    #日志相关
    url('echo_log', views.android_echo_log), #查看日志

]