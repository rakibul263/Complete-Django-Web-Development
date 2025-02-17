from django.urls import path
from . import views

urlpatterns = [
    path("courses/",views.courses),
    path("about/",views.about_section),
    path("", views.first_app_section),
]
