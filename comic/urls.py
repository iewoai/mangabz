from django.urls import path,re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path('(\w+)bz/', views.detail, name="detail"),
    re_path('chapter-(\w+)-s(1|2)/', views.chapter, name="chapter"),
]