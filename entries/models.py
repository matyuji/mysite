
# -*- encoding: utf-8 -*-

#=====================================================
# @file  :
# @breaf :
#=====================================================

#--------- import ---------
from django.db import models

#------------------------------------------------
# @class : Entry
# @breaf :
#------------------------------------------------
from django.forms.models import ModelForm

class Entry(models.Model):

    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 1000)
    user = models.IntegerField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/entries/detail/%i" % self.id

class EntryForm(ModelForm):
    class Meta:
        model = Entry


class Comment(models.Model):

    entry = models.ForeignKey(Entry)
    user_name   = models.CharField( max_length=50, blank=True)
    user_email  = models.EmailField( blank=True)
    user_url    = models.URLField( blank=True)
    comment = models.TextField( max_length=3000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/entries/detail/%i" % self.id

class CommentForm(ModelForm):
    class Meta:
        model = Comment


