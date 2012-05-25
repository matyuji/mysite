# -*- coding: utf-8 -*-
#
from django.shortcuts import get_object_or_404, render_to_response
from models import Entry, EntryForm
from django.http import HttpResponseRedirect

def object_list( request):
    list = None
    try:
        list = Entry.objects.filter( user=request.user.id)
    except Entry.DoesNotExist:
        list = []
    return render_to_response( "entries/entry_list.html", { 'request':request, 'object_list':list});

def create_object( request, model, post_save_redirect):
    if request.method == 'POST':
        new_data =request.POST.copy()
        form = EntryForm(new_data)
        if form.is_valid():
            obj = form.save();
            return HttpResponseRedirect( obj.get_absolute_url())

    else:
        pass
        form = EntryForm()
    d = dict(form=form, user_id = request.user.id)
    return render_to_response("entries/entry_form.html", d)