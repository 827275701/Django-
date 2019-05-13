from django.shortcuts import render
from django.shortcuts import HttpResponse

def admin_index(request):
    return render(request, "admin/admin.html", )

def android_login(request):
    return HttpResponse('yes')

def android_choose_spot(request):
    return HttpResponse('lhw&001')

def android_now_data(request):
    return HttpResponse('24&s37&2.1')

def android_person_info(request):
    return HttpResponse('lhwie&001&20&man&18165151223')

def android_history(request):
    return HttpResponse('20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20&20')

def android_add_user(request):
    return HttpResponse("test_add_user")