from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from hello.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
import turtle
import time
import random
# Create your views here.
def home(request):
    
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,'home.html')
def button1(request):
     return render(request,'button1.html')  
def output(request):
     delay=0.1
     score=0
     high_score=0
     wn=turtle.Screen()
     wn.title("snake game")
     wn.bgcolor("black")
     wn.setup(width=600,height=600)
     wn.tracer(0)
     head=turtle.Turtle()
     head.speed(0)
     head.color("white")
     head.shape('square')
     head.goto(0,0)
     head.direction="stop"
     food=turtle.Turtle()
     colors=random.choice(['red','blue','green'])
     shapes=random.choice(['square','circle','triangle'])
     food.speed(0)
     food.shape(shapes)
     food.color(colors)
     food.penup()
     food.goto(0,100)
     segments=[]
     pen=turtle.Turtle()
     pen.speed(0)
     pen.shape("square")
     pen.color("white")
     pen.penup()
     pen.hideturtle()
     pen.goto(0,250)
     pen.write("score:0 High score :0",align="center",font=("arial",24,"bold"))
     def goup():
          if head.direction!="down":
               head.direction="up"
     def godown():
          if head.direction!="up":
               head.direction="down"
     def goleft():
          if head.direction!="right":
               head.direction="left"
     def goright():
          if head.direction!="left":
               head.direction="right"
     def move():
          if head.direction=="up":
               y=head.ycor()
               head.sety(y+20)
          if head.direction=="up":
               y=head.ycor()
               head.sety(y+20)
          if head.direction=="left":
               x=head.xcor()
               head.setx(x-20)   
          if head.direction=="right":
               x=head.xcor()
               head.setx(x+20)    




     wn.listen()
     wn.onkeypress(goup,"w")
     wn.onkeypress(godown,"s")
     wn.onkeypress(goleft,"a")
     wn.onkeypress(goright,"d")
     wn.mainloop()

     while True:
          wn.update()
          if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
               time.sleep(1)
               head.goto(0,0)
               head.direction="stop"
               colors=random.choice(['red','blue','green'])
               shapes=random.choice(['square','circle','triangle'])
               for segment in segments:
                    segment.goto(1000,1000)
               segments.clear()
               score=0
               delay=0.1
               pen.clear()
               pen.write("score:{} High score :{}".format(score,high_score),align="center",font=("arial",24,"bold"))  
        

          if head.distance(food)<20:
               x=random.randint(-270,270)
               y=random.randint(-270,270)
               food.goto(x,y)

               new_segment=turtle.Turtle()
               new_segment.speed(0)
               new_segment.shape("square")
               new_segment.color("grey")
               segment.append(new_segment)
               delay-=0.001
               score+=10
               if score>high_score:
                    high_score=score
               pen.clear()
               pen.write("score:{} High score :{}".format(score,high_score),align="center",font=("arial",24,"bold"))  
     

          for index in range(len(segments)-1,0,-1):
               x=segments[index-1].xcor()
               y=segments[index-1].ycor()
               segments[index].goto(x,y)
          if len(segments)>0:
               x=head.xcor()
               y=head.ycor()
               segments[index].goto(x,y)
          move()
          for segment in segments:
               if segment.distance(head)<20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction="stop"
                    colors=random.choice(['red','blue','green'])
                    shapes=random.choice(['square','circle','triangle'])
                    for segment in segments:
                         segment.goto(1000,1000)

                    segment.clear()
                    score=0 
                    delay=0.1
                    pen.clear()
                    pen.write("score:{} High score :{}".format(score,high_score),align="center",font=("arial",24,"bold"))  
     

          time.sleep(delay)
          
     return render(request,'button1.html')

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
         
        
               
          user = authenticate(username=username, password=password)
            

          if user is not None:
              
              
               login(request,user)
               return redirect("/")
          else:
                return render(request,'login.html')   

     return render(request,'login.html')   
def logoutuser(request):
     logout(request)
     return redirect("/login")


