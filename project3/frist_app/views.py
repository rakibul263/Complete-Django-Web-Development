from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author': 'Rahim', 'age' : 15, 'list' : ['Python', 'is', 'best'], 'birthday' : datetime.datetime.now(),'val':24 ,'courses' : [
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

        ], 'name': 'daffodil', 'myname' : 'S h u v o', 'firstAndLast' : ['Shuvo', 'Aysha', 'Priya', 'Halima', 'Shopna', 'Zaidur'], 'university' : 'daffodil international university'}
    return render(request, 'home.html', d);