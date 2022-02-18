from django.contrib import admin
from django.urls import path
from drf import views

urlpatterns = [
    # users urls
    path('', views.index, name='index'),
    path('login', views.adminlogin, name='login'),
    path('register', views.handleSignup, name='register'),
    path("logout/", views.adminlogout, name='logout'),
    # blogging urls
    path("blog", views.blog, name='blog'),
    path("blogPost<str:slug>", views.blogPost, name='blogPost'),
    path("add_blog", views.add_blog, name='add_blog'),
    path("edit_blog", views.edit_blog, name='edit_blog'),
    path("delete_blog", views.delete_blog, name='delete_blog'),
]