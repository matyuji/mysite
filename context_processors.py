
# -*- encoding: utf-8 -*-
from django.conf import settings
def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}

def static(request):
    return {'STATIC_URL': settings.STATIC_URL}

