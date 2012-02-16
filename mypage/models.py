# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
import datetime

class FacePhoto(models.Model):
    name = models.CharField(max_length=200,unique=True)
    image = models.ImageField("写真", upload_to='photos')

class Request(models.Model):
    pub_date = models.DateTimeField()
    username = models.CharField(max_length=200)
    req_user = models.CharField(max_length=200)
    question = models.CharField(max_length=200)

class FacePhotoAdmin(admin.ModelAdmin):
    pass

#admin.site.register(FacePhoto, FacePhotoAdmin)
#admin.site.register( Request)


