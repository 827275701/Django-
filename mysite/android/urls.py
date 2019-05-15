from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('admin', views.admin_index),
    url('login', views.android_login),
    url('choose_spot', views.android_choose_spot),
    url('now_data', views.android_now_data),
    url('person_info', views.android_person_info),
    url('history', views.android_history),
    url('add_user', views.android_add_user),
    url('change_password', views.android_change_password),
    url('delete_user', views.android_delete_user),
    url('select_user', views.android_select_user),
    url('change_other_password', views.android_admin_change_other_password),
    url('test_choose_spot', views.android_test_choose_spot),

]