
## -*- coding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @breaf : URLリンク定義
#=====================================================

#--------- import ---------
from django.conf.urls.defaults import *

#--------- query ---------

#--------- entries ---------
urlpatterns = patterns('',
    ( r'^$', 'oauth.views.get' ),
    ( r'^get_callback/$', 'oauth.views.get_callback' ),
    ( r'^success/$', 'django.views.generic.simple.direct_to_template', {'template':'./oauth/success.html'}),
    ( r'^failed/$', 'django.views.generic.simple.direct_to_template', {'template':'./oauth/failed.html'}),
)