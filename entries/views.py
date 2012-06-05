# -*- coding: utf-8 -*-
#
from django import forms
import django
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
#from django import newforms as forms
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from tweepy.error import TweepError
from entries.models import CommentForm, Comment
from models import Entry, EntryForm
from django.http import HttpResponseRedirect
from oauth.views import CONSUMER_KEY, CONSUMER_SECRET
import tweepy

def object_list( request):
    list = None
    try:
        list = Entry.objects.filter( user=request.user.id)
    except Entry.DoesNotExist:
        list = []
    return render_to_response( "entries/entry_list.html", {'object_list':list});

def create_object( request, model, post_save_redirect):
    if request.method == 'POST':
        new_data =request.POST.copy()
        form = EntryForm(new_data)
        if form.is_valid():
            key = request.session.get('key')
            secret = request.session.get('secret')
            if (key != None) and (secret != None):
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                auth.set_access_token( key, secret)
                api = tweepy.API(auth_handler=auth)
                tweet = request.POST["content"]
                try:
                    api.update_status(tweet)
                except TweepError: pass
            obj = form.save();
            return HttpResponseRedirect( obj.get_absolute_url())

    else:
        pass
        form = EntryForm()
    d = dict(form=form, user_id = request.user.id)

    return render_to_response("entries/entry_form.html", d)

def object_detail( request, object_id):
    if request.method == 'GET':
        data = request.GET.copy()
        form = CommentForm()
        if request.user.is_authenticated():
            if not data.get('name', ''):
                data["user_name"] = request.user.get_full_name() or request.user.username
            if not data.get('email', ''):
                data["user_email"] = request.user.email
            form = CommentForm(data)
    else:
        data = request.POST.copy()
        data['entry'] = object_id
        form = CommentForm( data)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse('entries.views.object_detail',args=[object_id]))

    comment_list = Comment.objects.filter(entry=object_id)
    obj = Entry.objects.get(id=object_id)
    return render_to_response("entries/entry_detail.html", { 'object':obj,'form':form, 'comm_list':comment_list })

def update_object( request, object_id, model):
    entry = get_object_or_404( Entry, pk=object_id)
    EntryInstanceForm = EntryForm(instance=entry)

    if request.method == 'POST':
        new_data = request.POST.copy()
        form = EntryForm(new_data)
        form.instance.id = int(object_id)
        if form.is_valid():
            obj = form.save()
#            obj = form.save(commit=False)
#            obj.created=entry.created
#            obj.save()
            return HttpResponseRedirect(obj.get_absolute_url())
    else:
        form = EntryInstanceForm
    d = dict( form=form,object=entry, user_id=request.user.id, id=object_id)

    return render_to_response( 'entries/entry_form.html',d)

def delete_object( request, object_id, model, post_delete_redirect):
    entry = get_object_or_404( Entry, pk=object_id)

    if request.method == 'POST':
         entry.delete()
         return HttpResponseRedirect(entry.get_absolute_url())

    d = dict( object=entry)

    return render_to_response( 'entries/entry_confirm_delete.html',d)


@csrf_protect
@require_POST
def post_comment(request, next=None, using=None):

    if request.method == 'GET':
        data = request.GET.copy()
        if request.user.is_authenticated():
            if not data.get('name', ''):
                data["name"] = request.user.get_full_name() or request.user.username
            if not data.get('email', ''):
                data["email"] = request.user.email

    list = None
    try:
        list = Entry.objects.filter( user=request.user.id)
    except Entry.DoesNotExist:
        list = []
    return render_to_response( "entries/entry_list.html", {'object_list':list});

