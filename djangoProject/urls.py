"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import HttpResponse
from django.urls import path
from app01 import views


def home(request):
    return HttpResponse("Hello World!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("s", home),
    path("index/", views.index),

    path("user/list/", views.user_list),

    path("news/", views.news_list),

    path("login/", views.login),

    path("orm/", views.orm),

    path("check/", views.check),

    path("delete/", views.delete),
]
