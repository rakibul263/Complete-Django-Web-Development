from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author': 'Rahim', 'age' : 15, 'list' : [1,2,3,4,5], 'courses' : [
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'C programming',
            'fee' : 1200
        }

        ]}
    return render(request, 'home.html', d);