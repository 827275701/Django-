from django.conf.urls import url, include

from . import views

urlpatterns = [
    #普通用户
    url('login', views.android_login),
    url('choose_spot', views.android_choose_spot),
    url('now_data', views.android_now_data),
    url('person_info', views.android_person_info),
    url('history_day', views.android_history_day),
    url('history_week', views.android_history_week),
    url('history_month', views.android_history_month),
    url('history_year', views.android_history_year),
    url('change_password', views.android_change_password),

    #admin
    url('admin', views.admin_index),

    #用户相关
    url('add_user', views.android_add_user),
    url('delete_user', views.android_delete_user),
    url('select_user', views.android_select_user),
    url('change_other_password', views.android_admin_change_other_password),

    #博览室相关
    url('get_room', views.android_get_room),#获得当前已存在博览室的 名称和ID，实现下拉菜单


    #日志相关
    url('echo_log', views.android_echo_log), #查看日志

]