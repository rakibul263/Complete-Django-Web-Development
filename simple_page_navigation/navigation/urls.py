from . import views
from django.urls import path, include

urlpatterns =[
    # path('', views.)
    path('about/', views.about),
    path('contact/', views.contact),
]