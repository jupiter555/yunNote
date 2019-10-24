from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *

# Create your views here.
def reg_view(request):

    if request.method == 'GET':
        #渲染页面
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        #处理 注册逻辑 【处理提交的数据】
        username = request.POST.get('username')
        if not username:
            #没提交用户名
            return HttpResponse('请输入用户名')

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not password1 or not password2:
            #密码未提交
            return HttpResponse('请输入密码')
        if password1 != password2:
            #两次密码不相等
            return HttpResponse('两次输入密码不一致')

        #判断用户名
        old_users = User.objects.filter(username=username)
        #如果有，则证明用户名已注册
        if old_users:
            return HttpResponse('当前用户名已注册')

        #创建用户
        try:
            user = User.objects.create(username=username, password=password1)
        except Exception as e:
            print('reg error')
            return HttpResponse('当前用户名已注册')

        #存cookies
        resp = HttpResponse('注册成功')
        resp.set_cookie('username', username, 60*60*24)
        resp.set_cookie('uid', user.id,60*60*24)
        return resp

    return HttpResponse('test is ok')

def login_view(request):
    #登录
    if request.method == 'GET':
        #1,检查session
        if 'username' in request.session and 'uid' in request.session:
            #已经登录
            return HttpResponseRedirect('/user/index')

        #2, 检查cookies
        if 'username' in request.COOKIES and 'uid' in request.COOKIES:
            #已登录 & session没数据
            #回写session并让用户跳转至首页
            request.session['username'] = request.COOKIES['username']
            request.session['uid'] = request.COOKIES['uid']
            return HttpResponseRedirect('/user/index')

        return render(request, 'user/login.html')
    elif request.method == 'POST':
        #处理登录提交的数据

        #检查用户是否点击 下次免登陆
        save_cookies = False
        if 'save_cookies' in request.POST.keys():
            save_cookies = True

        username = request.POST.get('username')
        if not username:
            dic = {'msg': '请提交用户名'}
            return render(request, 'user/login.html',dic)
        password = request.POST.get('password')
        if not password:
            dic = {'msg': '请提交密码'}
            return render(request, 'user/login.html', dic)
        #查找用户
        user = User.objects.filter(username=username)
        if not user:
            print('---user login %s 用户名不存在'%(username))
            dic = {'msg': '用户名或密码错误'}
            return render(request, 'user/login.html', dic)
        if user[0].password != password:
            print('---user login  %s 密码不正确'%(username))
            dic = {'msg': '用户名或密码错误'}
            return render(request, 'user/login.html',dic)
        #用户和密码均匹配
        #记录登录状态
        request.session['username'] = username
        request.session['uid'] = user[0].id

        #检查是否存储cookies
        resp = HttpResponseRedirect('/user/index')
        if save_cookies:
            #cookies中存储用户登录状态 时长30天
            resp.set_cookie('username', username, 60*60*24*30)
            resp.set_cookie('uid', user[0].id, 60*60*24*30)
        return resp


def index(request):
    #首页
    print('-----user index------')
    print(request.session.get('username'))
    print(request.session.get('id'))

    username = request.session.get('username')
    if 'username' in request.session and 'uid' in request.session:
        #已登录
        is_login = True
    else:
        #未登录
        is_login = False
    print(is_login)
    print('-----user index over------')
    return render(request, 'user/index.html', locals())


def logout_view(request):
    #登出
    #删除cookies
    #删除session
    #302跳转至 /user/index
    if 'username' in request.session and 'uid' in request.session:
        del request.session['username']
        del request.session['uid']

    resp = HttpResponseRedirect('/user/index')
    if 'username' in request.COOKIES and 'uid' in request.COOKIES:
        resp.delete_cookie('username')
        resp.delete_cookie('uid')

    return resp

























































