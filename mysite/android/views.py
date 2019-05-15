from django.shortcuts import render
from django.shortcuts import HttpResponse

def admin_index(request):
    return render(request, "admin/admin.html", )

def android_login(request):
    print(request.body)
    return HttpResponse('yes')

def android_choose_spot(request):
    print(request.body)
    return HttpResponse('name=lhw&no=001')

def android_now_data(request):
    print(request.body)
    return HttpResponse('wendu=24&shidu=37&qiti=2.1')

def android_person_info(request):
    print(request.body)
    return HttpResponse('name=lhwie&no=001&age=20&sex=man&phone=18165151223')

def android_history(request):
    print(request.body)
    return HttpResponse('qiti=20&21&20&21&20&21&21&21&21&21&20&20&20&22&20&25&20&25&20&20&21&22&23&24')

def android_add_user(request):
    print(request.body)
    return HttpResponse('test_add_user')

def android_change_password(request):
    print(request.body)
    return HttpResponse('Successful')

def android_delete_user(request):
    print(request.body)
    return HttpResponse('Successful')

def android_select_user(request):
    print(request.body)
    return HttpResponse('name=lhwie&no=001&phone=18165151223&name=lhwie&no=001&phone=18165151223&name=lhwie&no=001&phone=18165151223')

def android_admin_change_other_password(request):
    print(request.body)
    return HttpResponse('Successful')

def android_get_root(requesr):
    print(requesr.body)
    return HttpResponse('博览室1&博览室2')



