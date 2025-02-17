from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse('This is course page.');

def about_section(request):
    return HttpResponse('This is about section page.');

def first_app_section(request):
    return HttpResponse('This is a first page for this website');