from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('admin', views.admin_index),
    url('login', views.android_login),
    url('choose_spot', views.android_choose_spot),
    url('now_data', views.android_now_data),
    url('person_info', views.android_person_info),
    url('t_history', views.android_t_history),
    url('h_history', views.android_h_history),
    url('g_history', views.android_g_history),
    url('add_user', views.android_g_history),

]