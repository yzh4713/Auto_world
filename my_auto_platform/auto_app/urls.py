# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:Yzh不是拼命三郎
@PRODUCT_NAME:PyCharm
@PROJECT_NAME:my_auto_platform
@FileName: urls.py
@Time:2020/7/1 23:26
@Motto:没有什么不会的，只要你愿意去做
"""

from django.conf.urls import url
from auto_app import views

urlpatterns = [
    # ^匹配要检索的文本的开头,$匹配文本的结束
    url('^login/$', views.my_login,name='login'),# 删除$,那么访问链接则可以在index/后面乱加字符串,依然能访问成功
    url('^$',views.my_login,name='login'),
]