#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created by florije4ex / florije4ex@gmail.com at 2019/11/29.
Copyright to BIXIN GLOBAL Co.,Ltd.
"""

from django.conf.urls import url
from .views import HomePageView, AboutPageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^about/', AboutPageView.as_view(), name='about'),
]
