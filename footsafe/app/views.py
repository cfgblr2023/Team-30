from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'index.html')

def category(request):
    return render(request, 'Categories.html')

def contribute(request):
    return render(request, 'UserGuidelines.html')

def contactus(request):
    return render(request, 'ContactUs.html')