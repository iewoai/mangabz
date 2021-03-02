from django.urls import path,re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path('(\w+)/', views.detail, name="detail"),
]