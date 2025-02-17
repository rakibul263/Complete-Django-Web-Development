from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    dic = {'for_add' : 10, 
           'for_addslashes' : "I'm Shuvo", 
           'for_capfirst' : 'rakibul',
           'for_center' : "rakbibul hasan",
           'for_cut' : "Rakbibul Hasan",
           'for_date' : datetime.datetime.now(),
           'for_empty' : '',
           'for_dicsort' : [
               {'name' : 'rakibul', 'age' : 20},
               {'name' : 'Ahamed', 'age' : 21},
               {'name' : 'Hasan', 'age' : 23}
            ],
            'for_divisibleby' : 21,
            'for_filesizeformat' : 1024,
            'for_first_and_last' : ['jodu', 'modu', 'kodu'],
            'for_lower' : 'Daffodil International University',
            'for_title' : 'this is my home town.',



        }

    return render(request, 'home.html', dic);