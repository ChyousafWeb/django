from django.contrib import admin
from django.urls import path
from ProjectApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("back", views.index, name='back'),
    path("about", views.about, name='about'),
    path("shop", views.shop, name='shop'),
    path("vagetables", views.vagetables, name='vagetables'),
    path("blog", views.blog, name='blog'),
    path("contact", views.contact, name='contact'),
    path("contact", views.contact, name='contact'),
    path("Signup", views.Signup, name='Signup'), 
    path("login", views.login, name='login')
]