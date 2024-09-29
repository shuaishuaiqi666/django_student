from django.shortcuts import render, HttpResponse
from app01.models import Departments, UserInfo
import requests


# Create your views here.

def index(request):
    return HttpResponse("You're at the polls index.")


def user_list(request):
    return render(request, 'user_list.html')


def news_list(req):
    return render(req, 'news_list.html')


def login(request):  #注册
    if request.method == "GET":
        return render(request, '用户注册.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        UserInfo.objects.create(username=username, password=password, mobile=mobile)
        return HttpResponse("提交成功")


def check(request):
    data_list = UserInfo.objects.all()
    return render(request, '用户查询.html', {"data_list": data_list})


def delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    data_list = UserInfo.objects.all()
    return render(request, '用户查询.html', {"data_list": data_list})


def orm(request):
    Departments.objects.create(title="销售部")
    Departments.objects.create(title="维修部")
    Departments.objects.create(title="管理部")
    return HttpResponse("添加成功")
