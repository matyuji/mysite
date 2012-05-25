
## -*- coding: utf-8 -*-

#=====================================================
# @file  : urls.py
# @breaf : URLリンク定義
#=====================================================

#--------- import ---------
from django.conf.urls.defaults import *

#--------- URL ---------
urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'./account/login_success.html'} ),
    (r'^user_regist/$', 'account.views.regist'),
    (r'^regist_success/$', 'django.views.generic.simple.direct_to_template', {'template':'./account/regist_success.html'}),
    #
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name':'./account/login.html'}),
    #
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'./account/logout.html'} ),
)
