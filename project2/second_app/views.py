from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse('This is a Home page')
    # return render('templates')
    return render(request, 'second_app/home.html');