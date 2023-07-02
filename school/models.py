from django.shortcuts import render,redirect,reverse,get_object_or_404
from datetime import timezone
from django.utils import timezone as django_timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# razorpay_client = razorpay.Client(auth=('', ''))

class imageinsert(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=100)
    preditions = models.CharField(max_length=100)
    def __str__(self):  
        return self.name







