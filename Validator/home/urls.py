from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.home1,name='home1'),
    path("index", views.index,name='index'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("contact",views.contact,name='contact'),
    
]