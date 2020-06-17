from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import Student, Admin, Leader
from django.template.context_processors import csrf
import json
import time
import hashlib

def get_csrf(request):
    # 生成 csrf 数据，发送给前端
    x = csrf(request)
    csrf_token = x['csrf_token']
    print(csrf_token)
    return HttpResponse(str(csrf_token))


# Create your views here.
def login_check(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    result_find = {}
    if request.method == 'GET':
        return HttpResponse('get')
    try:
        userid_get = request.POST.get('userid', '')
        pwd_get = request.POST.get('password', '')
        identity_get = request.POST.get('identity', '')
        if identity_get == 'student':
            result_find = Student.objects.filter(userid=userid_get)
        elif identity_get == 'admin':
            result_find = Admin.objects.filter(userid=userid_get)
        elif identity_get == 'leader':
            result_find = Leader.objects.filter(userid=userid_get)
        """
        result为<class 'django.db.models.query.QuerySet'>的对象
        需要进行数据处理
        """
        if len(result_find) == 1:
            pwd = result_find[0].password
            if pwd == pwd_get:
                cur_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                result_response['status'] = 1
                result_response['msg'] = '登录成功'
                result_response['logintime'] = cur_time
                result_response['lastlogintime'] = result_find[0].logintime
                result_response['jointime'] = result_find[0].jointime
                result_response['username'] = result_find[0].username
                # 保存最近登录时间
                result_find[0].logintime = cur_time
                result_find[0].save()
            else:
                result_response['status'] = 2
                result_response['msg'] = '密码错误'
        else:
            result_response['status'] = 3
            result_response['msg'] = '用户名不存在'
    except Exception as error:
        print(error)
        result_response['status'] = 4
        result_response['msg'] = '不可预料的错误'
    return JsonResponse(result_response)


def add_person(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    if request.method == 'GET':
        return HttpResponse('get')
    num_succ = 0
    num_fail = 0
    try:
        userid_get = request.POST.get('userid', '')
        identity_get = request.POST.get('identity', '')
        data_get = json.loads(request.POST.get('data', ''))
        type_get = request.POST.get('type', '')
        for person in data_get:
            print(person)
            print(person['学号'])
            print(person['姓名'])
            pwd = hashlib.md5(str(person['密码']).encode()).hexdigest()
            print(pwd)
            try:
                stu_new = Student()
                stu_new.userid = person['学号']
                stu_new.username = person['姓名']
                stu_new.password = pwd
                stu_new.jointime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                stu_new.save()
                num_succ += 1
            except Exception as error:
                print(error)
                num_fail += 1
        if num_fail > 0:
            result_response['status'] = 2
            result_response['msg'] = '学生信息: ' + str(num_succ) + '人添加成功, ' + str(num_fail) + '人已存在。'
        else:
            result_response['status'] = 1
            result_response['msg'] = '学生信息添加成功'
    except Exception as error:
        print(error)
        result_response['status'] = 0
        result_response['msg'] = '学生信息添加失败'
    return JsonResponse(result_response)


def get_person(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    try:
        records = []
        num = 1
        result = Student.objects.all()
        for i in result:
            try:
                logintime = i.logintime
                if not logintime:
                    logintime = '无登录记录'
                record = {
                    'userid': i.userid,
                    'username': i.username,
                    'logintime': logintime,
                    'jointime': i.jointime,
                    'index': num,
                }
                records.append(record)
            except Exception as error:
                print(error)
            num += 1
        result_response['status'] = 1
        result_response['msg'] = '刷新成功'
        result_response['records'] = records
    except Exception as error:
        print(error)
        result_response['msg'] = '刷新失败'
    return JsonResponse(result_response)


def delete_person(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    try:
        userid_get = request.POST.get('userid', '')
        row = Student.objects.get(userid=userid_get)
        row.delete()
        result_response['status'] = 1
        result_response['msg'] = '删除用户' + '' + '成功'
    except Exception as error:
        print(error)
        result_response['msg'] = '删除失败'
    return JsonResponse(result_response)


def change_password(request):
    result_response = {
        'status': 0,
        'msg': '操作失败',
    }
    result_find = {}
    if request.method == 'GET':
        return HttpResponse('get')
    try:
        userid_get = request.POST.get('userid', '')
        identity_get = request.POST.get('identity', '')
        password_get = request.POST.get('password', '')
        password_new_get = request.POST.get('password_new', '')
        if identity_get == 'student':
            result_find = Student.objects.get(userid=userid_get)
        elif identity_get == 'admin':
            result_find = Admin.objects.get(userid=userid_get)
        elif identity_get == 'leader':
            result_find = Leader.objects.get(userid=userid_get)
        if result_find.password == password_get:
            result_find.password = password_new_get
            result_find.save()
            result_response['status'] = 1
            result_response['msg'] = '修改密码成功'
        else:
            result_response['status'] = 2
            result_response['msg'] = '原密码错误'
    except Exception as error:
        print(error)
        result_response['status'] = 3
        result_response['msg'] = '不可预料的错误'
    return JsonResponse(result_response)
