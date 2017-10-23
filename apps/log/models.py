from __future__ import unicode_literals
from django.db import models

class users(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    age=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# Create your models here.
