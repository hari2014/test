# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class detail(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100)
    password=models.CharField(max_length=100, default='')

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)