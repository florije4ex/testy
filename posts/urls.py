#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created by florije4ex / florije4ex@gmail.com at 2019/11/29.
Copyright to BIXIN GLOBAL Co.,Ltd.
"""

from django.conf.urls import url

from .views import PostPageView

urlpatterns = [
    url(r'^$', PostPageView.as_view(), name='posts'),
]
