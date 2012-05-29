
# -*- coding: utf-8 -*-

#=====================================================
# @file  : view.py
#=====================================================

#--------- import ---------
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import tweepy

CONSUMER_KEY = 'I92fMef2R6hruNCoCWaAQ'
CONSUMER_SECRET = 'eb3qYqWcIsVibZKkX0kA7cqDvXcApQsmd95dHNMBM'
CALLBACK_URL = 'http://127.0.0.1:8000/oauth/get_callback/'

#------------------------------------------------
def get(request):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)

    try:
        auth_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'

    request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)
    return HttpResponseRedirect(auth_url)


#------------------------------------------------
def get_callback(request):
    # Example using callback (web app)
    verifier = request.GET.get('oauth_verifier')

    # Let's say this is a web app, so we need to re-build the auth handler first...
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    token = request.session.get('request_token')
    del request.session['request_token']
    auth.set_request_token(token[0], token[1])

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'
        return HttpResponseRedirect('../failed')

    request.session['key'] = auth.access_token.key
    request.session['secret'] = auth.access_token.secret
#    return HttpResponseRedirect(reverse('mysite.oauth.views.oauth_index'))
    return HttpResponseRedirect('../success')



