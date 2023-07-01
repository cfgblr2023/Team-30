from django.shortcuts import render
from django.shortcuts import render,redirect,reverse,get_object_or_404
from . import models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home_view(request):
    # if request.user.is_authenticated:
    print("hello")
    return reverse(request,'index.html')
    # return render(request,'school/index.html')

