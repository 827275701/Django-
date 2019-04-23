from django.shortcuts import render
from django.shortcuts import HttpResponse

def admin_index(request):
    return render(request, "admin/admin.html", )

def android_login(request):
    return HttpResponse('yes')

def android_choose_spot(request):
    return HttpResponse('name=xxx&number=001')

def android_now_data(request):
    return HttpResponse('wendu=24&shidu=37&qiti=2.5')

def android_person_info(request):
    return HttpResponse('lhwie&001&20&man&2015-2-14&1777-10-21&xxxxxxxxx')

