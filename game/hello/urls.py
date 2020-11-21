
from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
  path('',views.home, name='home'),
 
 
  path('about',views.about,name='about'),
  path('contact',views.contact,name='contact'),
  path('login',views.loginuser,name='loginuser'),
  path('logout',views.logoutuser, name='logoutuser'),
  path('button1',views.button1),
  path('button1',views.output,name='game1'),
  path('',views.button1),
  path('',views.output,name='game1'),
  path('',views.button1),
  path('',views.output,name='game1'),
  path('',views.button1),
  path('',views.output,name='game1')

  
]