from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
import time
import json
import os
from lab_manage import settings
from django.template.context_processors import csrf
import urllib.parse

from .models import Trs, Plst, Ravt, Ucst, Rtst, Tcst, Rdst, Irms, Bot


# Create your views here.
def add(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    if request.method == 'GET':
        return HttpResponse('error with method get')
    userid_get = request.POST.get('userid', '')
    data_get = str(request.POST.get('data', ''))
    type_get = request.POST.get('type', '')
    identity_get = request.POST.get('identity', '')
    try:
        table = ''
        if type_get == 'trs':
            table = Trs()
        elif type_get == 'plst':
            table = Plst()
        elif type_get == 'ravt':
            table = Ravt()
        elif type_get == 'ucst':
            table = Ucst()
        elif type_get == 'rtst':
            table = Rtst()
        elif type_get == 'tcst':
            table = Tcst()
        elif type_get == 'rdst':
            table = Rdst()
        elif type_get == 'irms':
            table = Irms()
        table.userid = userid_get
        table.data = data_get
        table.time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        table.save()
        result_response['status'] = 1
        result_response['msg'] = '记录添加成功'
    except Exception as error:
        print(error)
        result_response['msg'] = '记录添加失败'
    return JsonResponse(result_response)


def change(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    if request.method == 'GET':
        return HttpResponse('error with method get')
    print(request.POST)
    userid_get = request.POST.get('userid', '')
    data_get = json.loads(request.POST.get('data', ''))
    type_get = request.POST.get('type', '')
    identity_get = request.POST.get('identity', '')
    try:
        table = ''
        if type_get == 'trs':
            table = Trs
        elif type_get == 'plst':
            table = Plst
        elif type_get == 'ravt':
            table = Ravt
        elif type_get == 'ucst':
            table = Ucst
        elif type_get == 'rtst':
            table = Rtst
        elif type_get == 'tcst':
            table = Tcst
        elif type_get == 'rdst':
            table = Rdst
        elif type_get == 'irms':
            table = Irms
        row = table.objects.get(userid=userid_get, time=data_get['time'])
        row.data = json.dumps(data_get)
        row.time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        row.save()
        result_response['status'] = 1
        result_response['msg'] = '记录修改成功'
    except Exception as error:
        print(error)
        result_response['msg'] = '记录修改失败'
    return JsonResponse(result_response)


def add_bot(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    base_url = 'http://127.0.0.1:8000/static/tables/'
    if request.method == 'GET':
        return HttpResponse('error with method get')
    data = json.loads(request.POST.get('data', ''))
    file_upload = request.FILES.get('files[]', '')
    try:
        userid_get = data['userid']
        data_get = data['data']
        current_time = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        file_name = os.path.join(settings.STATICFILES_DIRS[0], 'tables', current_time + '-' + file_upload.name)
        with open(file_name, 'wb') as file:
            for chunk in file_upload.chunks():
                file.write(chunk)
        image_url = os.path.join(base_url, current_time + '-' + urllib.parse.quote(file_upload.name))
        bot = Bot()
        bot.userid = userid_get
        bot.data = data_get
        bot.time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        bot.img = image_url
        bot.save()
        result_response['status'] = 1
        result_response['msg'] = '记录添加成功'
    except Exception as error:
        print(error)
        result_response['msg'] = '记录添加失败'
    return JsonResponse(result_response)


def change_bot(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    base_url = 'http://127.0.0.1:8000/static/tables/'
    if request.method == 'GET':
        return HttpResponse('error with method get')
    data = json.loads(request.POST.get('data', ''))
    file_upload = request.FILES.get('files[]', '')
    try:
        userid_get = data['userid']
        data_get = data['data']
        time_get = data['time']
        current_time = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        print(data_get)
        print(json.loads(data_get))
        bot = Bot.objects.get(userid=userid_get, time=time_get)
        if file_upload != '':
            file_name = os.path.join(settings.STATICFILES_DIRS[0], 'tables', current_time + '-' + file_upload.name)
            with open(file_name, 'wb') as file:
                for chunk in file_upload.chunks():
                    file.write(chunk)
            image_url = os.path.join(base_url, current_time + '-' + urllib.parse.quote(file_upload.name))
            bot.img = image_url
        bot.data = data_get
        bot.time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        bot.save()
        result_response['status'] = 1
        result_response['msg'] = '记录修改成功'
    except Exception as error:
        print(error)
        result_response['msg'] = '记录修改失败'
    return JsonResponse(result_response)


def add_comment(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    if request.method == 'GET':
        return HttpResponse('error with method get')
    try:
        userid_get = request.POST.get('userid', '')
        identity_get = request.POST.get('identity', '')
        comment_get = request.POST.get('comment', '')
        time_get = request.POST.get('time', '')
        stuid_get = request.POST.get('stuid', '')
        current_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        trs = Trs.objects.filter(userid=stuid_get, time=time_get)
        if len(trs) != 1:
            raise Exception('counts error')
        if identity_get == 'admin':
            trs[0].admin = json.dumps({
                'userid': userid_get,
                'comment': comment_get,
                'time': current_time,
            })
            trs[0].save()
        else:
            trs[0].leader = json.dumps({
                'userid': userid_get,
                'comment': comment_get,
                'time': current_time,
            })
            trs[0].save()
        print(len(trs))
        result_response['status'] = 1
        result_response['msg'] = '审核意见添加成功'
    except Exception as error:
        print(error)
        result_response['msg'] = '审核意见添加失败'
    return JsonResponse(result_response)


def equipment_using_record(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    try:
        records = []
        result = Trs.objects.filter()
        num = 1
        for i in result:
            record = {
                'index': num,
                'zyyqsb': json.loads(i.data)['zyyqsb'],
                'syry': json.loads(i.data)['syry'],
            }
            num += 1
            # content = {'学号': i.studentNum, '姓名': i.name, '性别': i.sex}
            records.append(record)
        result_response['status'] = 1
        result_response['msg'] = '刷新成功'
        result_response['records'] = records
    except Exception as error:
        print(error)
        result_response['msg'] = '刷新失败'
    return JsonResponse(result_response)


def ear_records(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    try:
        userid = request.GET.get('userid', '')
        records = []
        num = 1
        if userid == '':
            result = Trs.objects.all()
        else:
            result = Trs.objects.filter(userid=userid)
        table_name, table_name_en = ('试验技术方案', 'trs')
        for i in result:
            try:
                admin_comment = ''
                leader_comment = ''
                if i.admin:
                    admin_comment = json.loads(i.admin)
                if i.leader:
                    leader_comment = json.loads(i.leader)
                record = {
                    'stu_id': i.userid,
                    'data': json.loads(i.data),
                    'type': table_name,
                    'type_en': table_name_en,
                    'time': i.time,
                    'admin': admin_comment,
                    'leader': leader_comment,
                    'index': num,
                }
                records.append(record)
                num += 1
            except Exception as error:
                print(error)
        result_response['status'] = 1
        result_response['msg'] = '刷新成功'
        result_response['records'] = records
    except Exception as error:
        print(error)
        result_response['msg'] = '刷新失败'
    return JsonResponse(result_response)


def trial_record(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    try:
        userid = request.GET.get('userid', '')
        records = []
        num = 1
        tables = [Plst, Ravt, Ucst, Rtst, Tcst, Rdst, Irms, Bot]
        for table in tables:
            if userid == '':
                result = table.objects.all()
            else:
                result = table.objects.filter(userid=userid)
            table_name, table_name_en = get_class_name(str(table))
            for i in result:
                try:
                    data = json.loads(i.data)
                    if table_name_en == 'irms' or table_name_en == 'bot':
                        data['syry'] = i.userid
                    record = {
                        'stu_id': i.userid,
                        'data': data,
                        'type': table_name,
                        'type_en': table_name_en,
                        'time': i.time,
                        'index': num,
                    }
                    if 'Bot' in str(table):
                        record['img'] = i.img
                    records.append(record)
                    num += 1
                except Exception as error:
                    print(error)
        result_response['status'] = 1
        result_response['msg'] = '刷新成功'
        result_response['records'] = records
    except Exception as error:
        print(error)
        result_response['msg'] = '刷新失败'
    return JsonResponse(result_response)


def delete_records(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    try:
        userid_get = request.POST.get('userid', '')
        time_get = request.POST.get('time', '')
        type_get = request.POST.get('type', '')
        table = ''
        if type_get == 'trs':
            table = Trs
        elif type_get == 'plst':
            table = Plst
        elif type_get == 'ravt':
            table = Ravt
        elif type_get == 'ucst':
            table = Ucst
        elif type_get == 'rtst':
            table = Rtst
        elif type_get == 'tcst':
            table = Tcst
        elif type_get == 'rdst':
            table = Rdst
        elif type_get == 'irms':
            table = Irms
        elif type_get == 'bot':
            table = Bot
        row = table.objects.get(userid=userid_get, time=time_get)
        row.delete()
        result_response['status'] = 1
        result_response['msg'] = '删除记录成功'
    except Exception as error:
        print(error)
        result_response['msg'] = '删除记录失败'
    return JsonResponse(result_response)


def get_class_name(table):
    if 'Trs' in table:
        return '试验技术方案', 'trs'
    elif 'Plst' in table:
        return '点荷载强度试验', 'plst'
    elif 'Ravt' in table:
        return '岩块声波速度测试', 'ravt'
    elif 'Ucst' in table:
        return '单轴抗压强度试验', 'ucst'
    elif 'Rtst' in table:
        return '岩石抗拉强度试验', 'rtst'
    elif 'Tcst' in table:
        return '三轴压缩强度试验', 'tcst'
    elif 'Rdst' in table:
        return '岩石直剪试验', 'rdst'
    elif 'Irms' in table:
        return '岩体结构调查', 'irms'
    elif 'Bot' in table:
        return '钻孔孔内观测试验', 'bot'
