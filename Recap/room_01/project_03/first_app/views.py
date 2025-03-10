from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author': "Rakiubl", 'age' : 10,'lst' :['python', 'is', 'best'], 'courses':[
            {
                'id' : 1,
                'name' : 'Python',
                'fee' : 5000,
            },
            {
                'id' : 2,
                'name' : 'CPP',
                'fee' : 6000,
            },
            {
                'id' : 3,
                'name' : 'JavaScript',
                'fee' : 7000,
            },
        ]}
    return render(request, 'home.html', d)