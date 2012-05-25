
# -*- coding: utf-8 -*-
#------------------------------------------------
# @breaf : ユーザー登録
#------------------------------------------------

#--------- import ---------
import os
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mysite.polls.models import Choice, Poll
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.db import IntegrityError
#--------- function ---------
def regist(request):

    try:
        name = request.POST['name']
        mail = ''#request.POST['mail']
        password = request.POST['pass']
        password2 = request.POST['pass2']

    except KeyError:
        return render_to_response('account/user_regist.html', context_instance=RequestContext(request) )
    else:
        try:
            user = User.objects.create_user( name, mail, password)
        except IntegrityError:
            return render_to_response('account/user_regist.html', {
                'error_message' : "指定のユーザは登録済みです。",
                }, context_instance=RequestContext(request) )
        except:
            return HttpResponseRedirect( '../user_regist', )
        else:
            if password != password2:
                return render_to_response('account/user_regist.html', {
                    'error_message' : "パスワードが一致しません。",
                    }, context_instance=RequestContext(request) )
            elif name == "" or name == None:
                return render_to_response('account/user_regist.html', {
                    'error_message' : "ユーザー名を入力してください。",
                    }, context_instance=RequestContext(request) )

#        return HttpResponseRedirect( '../login', { 'error_message' : "新規ユーザが登録されました。", })
        return HttpResponseRedirect( '../regist_success')
#        return HttpResponseRedirect( reverse( 'login', kwargs={'error_message':"新規ユーザが登録されました。",}))


    """
    p = get_object_or_404( Poll, pk=object_id )
    #------ 投票対象を選択しているか ------
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])

    #------ 否選択 ------
    except (KeyError, Choice.DoesNotExist):
        # 投票フォームを再表示
        return render_to_response('polls/detail.html', {
            'object': p,
            'error_message' : "選択肢を選んでいません。",
            }, context_instance=RequestContext(request) )

    #------ 選択中 ------
    else:
        # 投票状況を更新
        selected_choice.votes += 1
        selected_choice.save()
        vote = Vote()
        vote.choice = selected_choice
        if request.user.is_anonymous():
            vote.username = 'anonymous'
        else:
            vote.username = request.user.username
        vote.save()
        #    selected_choice.vote_set.
        # ユーザが Back ボタンを押して同じフォームを提出するのを防ぐ
        # ため、POST データを処理できた場合には、必ずHttpResponseRedirect を返すようにします。
        return HttpResponseRedirect( reverse( 'results', args=(p.id,)))
    """
