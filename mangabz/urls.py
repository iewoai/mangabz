"""mangabz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static
from django.conf.urls import url
from mangabz.settings import STATIC_ROOT
import comic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comic.urls')),
    re_path('(\w+)bz/', include('comic.urls')),
    re_path('chapter-(\w+)-s(1|2)/', include('comic.urls')),
    re_path('m(\w+)/', include('comic.urls')),
    re_path('m(\w+)/chapterimage.ashx?cid=<str:cid>&page=<str:page>&key=&_cid=<str:cid>&_mid=<str:mid>&_dt=<str:date>&_sign=<str:sign>', include('comic.urls')),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root':STATIC_ROOT}, name='static'),
]

# 定义错误跳转页面
handler404 = comic.views.page_not_found