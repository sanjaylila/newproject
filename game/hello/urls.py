
from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
  path('',views.home, name='home'),
 
 
  path('about',views.about,name='about'),
  path('contact',views.contact,name='contact'),
  path('login',views.loginuser,name='loginuser'),
  path('logout',views.logoutuser, name='logoutuser'),
  path('',views.button1),
  path('output1',views.output1,name='game1'),
  path('button2',views.button2),
  path('output2',views.output2,name='game2'),
  path('',views.button1),
  path('output1',views.output1,name='game1'),
  path('',views.button4),
  path('output4',views.output4,name='game4')

  
]