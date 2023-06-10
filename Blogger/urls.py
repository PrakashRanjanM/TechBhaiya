from django.contrib import admin
from django.urls import path
from Blogger import views
urlpatterns = [
    path('', views.BlogHome , name = "BlogHome"),
    path('blogComment', views.blogComment, name = 'blogComment'),
    path('<str:slug>', views.blogPost , name = "blogPost"),

]