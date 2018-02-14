# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


# Create your models here.
class UserProfile(models.Model):

    username = models.CharField(max_length=128)
    Department = models.CharField(default = 'Null',max_length=10)
    Year = models.IntegerField(default = 1)
    Time = models.CharField(max_length = 40,default=timezone.now().strftime("%d/%m/%Y %H:%M:%S"))
    def __str__(self):
    	return self.username