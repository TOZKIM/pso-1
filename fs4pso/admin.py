# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Subject, Comment

admin.site.register(Post)
admin.site.register(Subject)
admin.site.register(Comment)