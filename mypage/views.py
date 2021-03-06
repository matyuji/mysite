# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from mypage.models import FacePhoto
from mysite.polls.models import Poll
from mysite.mypage.models import Request
from django.http import Http404, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
import datetime
#------------------------------------------------
# @breaf : インデックス
#------------------------------------------------
def index(request):
    return render_to_response( 'mypage/index.html', { 'request': request } )

def homepage(request, username):
    account = User.objects.get(username=username)
    if not account:
        raise Http404
    photoname = ''
    try:
        obj = FacePhoto.objects.get(name=username)
    except:
        pass
    else:
        photoname = obj.image.name

    reqs = Request.objects.filter(req_user=username)
    return direct_to_template( request, 'mypage/homepage.html', { 'request': request, 'username':username, 'photoname':photoname, 'reqs':reqs })

def photo_upload(request):
    username = request.user.username
    if request.method == "POST":
        post_data = request.POST
        post_data.update(request.FILES)

        image_file = post_data["image_file"]
        if image_file:
            # すでにあれば削除
            try:
                obj = FacePhoto.objects.get(name=username)
            except:
                pass
            else:
                obj.delete()
            filename = image_file._name#["filename"]
            photo = FacePhoto()
            photo.name = username
            photo.image = filename
            photo.image.save(filename, image_file)#["content"])
            photo.save()
            return HttpResponseRedirect(reverse('result', kwargs=dict({'username':username,'resu':1})))
        else:
            return HttpResponseRedirect(reverse('result', kwargs=dict({'username':username,'resu':0})))
    else:
        message = ""

    return render_to_response('mypage/photo_upload.html', {'message': message,'username':username}, context_instance=RequestContext(request))#    return render_to_response('mypage/photo_upload.html', {'message': message,'username':username}, context_instance=RequestContext(request))

def result(request, username, resu):
    return render_to_response( 'mypage/result.html', { 'username':username,'resu':resu} )

def vote_request(request):
    username = request.user.username
    if request.method == "POST":
        post_data = request.POST
        req_user = post_data["username"]
        question = post_data["question"]
        if username and question:
            request = Request()
            request.pub_date = datetime.datetime.now()
            request.username = username
            request.req_user = req_user
            request.question = question
            request.save()
            return HttpResponseRedirect(reverse('result', kwargs=dict({'username':username,'resu':1})))
        else:
            return HttpResponseRedirect(reverse('result', kwargs=dict({'username':username,'resu':0})))
    else:
        message = ""

    users = User.objects.all()
    polls = Poll.objects.all()
    return render_to_response('mypage/vote_request.html', {'users':users, 'polls':polls, 'username':username}, context_instance=RequestContext(request))#    return render_to_response('mypage/photo_upload.html', {'message': message,'username':username}, context_instance=RequestContext(request))

