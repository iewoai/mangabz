from django.urls import path,re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r'^(\w+)bz/$', views.detail, name="detail"),
    re_path(r'^chapter-(\w+)-s(1|2)/$', views.chapter, name="chapter"),
    re_path(r'^m(?P<rowkey>\w+)(-p(?P<current_page>\w+))?/$', views.pages, name="pages"),
    re_path(r'm(?P<cid>\w+)(-p(?P<start_page>\w+))?/chapterimage.ashx', views.get_img_url_list, name="get_img_url_list"),
]