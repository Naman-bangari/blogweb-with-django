from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.home1,name='home1'),
    path("index", views.index,name='index'),
    path("full_review",views.full_review,name='full_review'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("auto_code",views.auto_code,name='auto_code'),
    path("about_us",views.about_us,name='about_us'),
]