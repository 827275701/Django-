from django.shortcuts import render
from django.shortcuts import HttpResponse

def admin_index(request):
    return render(request, "admin/admin.html", )

def android_login(request):
    print(request.body)
    return HttpResponse('Successful')

def android_choose_spot(request):
    print(request.body)
    return HttpResponse('name=lhw&no=001')

def android_now_data(request):
    print(request.body)
    return HttpResponse('wendu=24&shidu=37&qiti=2.1')

def android_person_info(request):
    print(request.body)
    return HttpResponse('name=lhwie&no=001&age=20&sex=man&phone=18165151223')

def android_history_day(request):
    print(request.body)
    return HttpResponse('qiti=20&21&20&21&20&21&21&21&21&21&20&20&20&22&20&25&20&25&20&20&21&22&23&24')

def android_history_week(request):
    print(request.body)
    return HttpResponse('qiti=20&21&20&21&20&21&21')

def android_history_month(request):
    print(request.body)
    return HttpResponse('qiti=20&21&20&21&20&21&21&21&21&21&20&20&20&22&20&25&20&25&20&20&21&22&23&24&20&20&21&22&23&24')

def android_history_year(request):
    print(request)
    return HttpResponse('qiti=20&21&20&21&20&21&21&21&21&21&20&20')

def android_add_user(request):
    print(request.body)
    return HttpResponse('Successful')

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

def android_admin_change_other_name(request):
    print(request.body)
    return HttpResponse("Successful")

def android_admin_change_other_no(request):
    print(request.body)
    return HttpResponse("Successful")

def android_admin_change_other_sex(request):
    print(request.body)
    return HttpResponse("Successful")

def android_get_room(request):
    print(request.body)
    return HttpResponse('room_id=room1&room_name=博览室1&room_id=room2&room_name=博览室2')

def android_echo_log(request):
    print(request.body)
    return  HttpResponse('log  test\nlog  test\nlog  test\nlog  test\nlog  test')

def android_change_other_info(request):
    print(request.body)
    return HttpResponse('Successful')

def android_get_person(request):
    print(request.body)
    return HttpResponse('name=路浩伟&no=123456&sex=男&phone=18165151223&pwd=123456')

def android_select_room(request):
    print(request.body)
    return HttpResponse('room_id=room1&room_name=博览室1&pos=6b220&room_id=room2&room_name=博览室2&pos=6b221&room_id=room3&room_name=博览室3&pos=6b222')

def android_get_the_room_info(request):
    print(request.body)
    return HttpResponse('room_id=room1&room_name=博览室1&pos=6b220&des=暂无记录')

def android_change_room_info(request):
    print(request.body)
    return HttpResponse('Successful')