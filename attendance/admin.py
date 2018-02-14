# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from import_export import resources

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

# Register your models here.


