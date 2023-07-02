from django.shortcuts import render,redirect,reverse,get_object_or_404
from datetime import timezone
from django.utils import timezone as django_timezone
from django.db import models
from django.contrib.auth.models import User

class userinsert(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.name
    
