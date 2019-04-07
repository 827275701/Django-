from django.db import models

# Create your models here.


'''
    创建 user pwd  两个字段，分别用来保存用户名和密码
    
    接下来在pycharm的teminal中通过命令创建数据库的表了。有2条命令，分别是：
        1、python manage.py makemigrations
        2、python manage.py migrate


'''
class UserInfo(models.Model):  #这个类需要继承models.Model
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

