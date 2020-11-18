from django.shortcuts import render,HttpResponse,render,redirect
from datetime import datetime
from hello.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout,login

# Create your views here.
def home(request):
     print(request.user)
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def contact(request):
     if request.method=='POST':

          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          desc=request.POST.get('desc')
          
          contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
          contact.save()
          messages.success(request, 'Your Message Has Been Sent!')
          
         
     
     return render(request,'contact.html')   
 
def loginuser(request):
     if request.method=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          user = User.objects.create_user(username=username,password=password)
          user.save()
         
          #user = authenticate(username=username, password=password)
          
          
         
          if user is not None:
              
               login(request,user)
               return redirect("/")
          else:
                return render(request,'login.html')   

     return render(request,'login.html')   
def logoutuser(request):
     logout(request)
     return redirect("/login")         