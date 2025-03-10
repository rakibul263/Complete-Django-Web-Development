from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("This is course space.")

def about(request):
    return HttpResponse("This is a About page for first App")

def first_app(request):
    return HttpResponse("This is a first app page in this project.");
