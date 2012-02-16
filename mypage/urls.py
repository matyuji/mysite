
# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *

# http://localhost:8000/polls/

#
urlpatterns = patterns( 'mypage.views',
    # トップ
    (r'^$', 'index'),
    (r'^home/(?P<username>.+)/$', 'homepage'),
    (r'^photo_upload/$', 'photo_upload'),
    (r'^vote_request/$', 'vote_request'),
    url( r'^result/(?P<username>.+)/(?P<resu>.+)/$', 'result', name='result'),
)