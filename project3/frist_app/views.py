from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author': 'Rahim', 'age' : 20, 'list' : [1,2,3,4,5]}
    return render(request, 'home.html', d);