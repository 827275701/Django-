from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('admin', views.admin_index),

]