from django.urls import path,re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r'^(\w+)bz/$', views.detail, name="detail"),
    re_path(r'^chapter-(\w+)-s(1|2)/$', views.chapter, name="chapter"),
    re_path(r'^m(\w+)/$', views.pages, name="pages"),
]