from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here.



def index(request):
    '''
    :param request: 这个参数必须有，名字类似以self的默认规则，可以改
                    他封装了用户请求的所有内容
    :return: 回复请求端的内容


    1、不能直接返回字符串，必须被封装起来，这是Django的规则，不是python,
        返回时使用from django.shortcuts import HttpResponse

    2、当想返回一个html文件是要用render来打包，这也是django的规则
        第一个参数，第二个参数是想发送的文件名
        为了是django知道html文件在哪，要在settings中来配置TEMPLATES中的DIRS
    '''
    #return HttpResponse("hello world")
    #return render(request, "index.html",)
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)

        #添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

    #从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
    '''
        总结数据库流程：
            1、导入包：from cmdb import models      
            2、添加数据到数据库
            3、进行数据库其他操作
    '''
    return render(request, "index.html", {"data": user_list})