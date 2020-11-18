
from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
  path('',views.home,name='home'),
  path('about',views.about,name='about'),
  path('contact',views.contact,name='contact'),
  path('login',views.loginuser,name='loginuser'),
  path('logout',views.logoutuser, name='logoutuser')
  
]