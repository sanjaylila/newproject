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
import tkinter as tk
word_list=[
    'wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'smite',
    'windy',
    'coin',
    'throw',
    'silence',
    'bluff',
    'downfall',
    'climb',
    'lying',
    'weaver',
    'snob',
    'kickoff',
    'match',
    'quaker',
    'foreman',
    'excite',
    'thinking',
    'mend',
    'allergen',
    'pruning',
    'coat',
    'emerald',
    'coherent',
    'manic',
    'multiple',
    'square',
    'funded',
    'funnel',
    'sailing',
    'dream',
    'mutation',
    'strict',
    'mystic',
    'film',
    'guide',
    'strain',
    'bishop',
    'settle',
    'plateau',
    'emigrate',
    'marching',
    'optimal',
    'medley',
    'endanger',
    'wick',
    'condone',
    'schema',
    'rage',
    'figure',
    'plague',
    'aloof',
    'there',
    'reusable',
    'refinery',
    'suffer',
    'affirm',
    'captive',
    'flipping',
    'prolong',
    'main',
    'coral',
    'dinner',
    'rabbit',
    'chill',
    'seed',
    'born',
    'shampoo',
    'italian',
    'giggle',
    'roost',
    'palm',
    'globe',
    'wise',
    'grandson',
    'running',
    'sunlight',
    'spending',
    'crunch',
    'tangle',
    'forego',
    'tailor',
    'divinity',
    'probe',
    'bearded',
    'premium',
    'featured',
    'serve',
    'borrower',
    'examine',
    'legal',
    'outlive',
    'unnamed',
    'unending',
    'snow',
    'whisper',
    'bundle',
    'bracket',
    'deny',
    'blurred',
    'pentagon',
    'reformed',
    'polarity',
    'jumping',
    'gain',
    'laundry',
    'hobble',
    'culture',
    'whittle',
    'docket',
    'mayhem',
    'build',
    'peel',
    'board',
    'keen',
    'glorious',
    'singular',
    'cavalry',
    'present',
    'cold',
    'hook',
    'salted',
    'just',
    'dumpling',
    'glimmer',
    'drowning',
    'admiral',
    'sketch',
    'subject',
    'upright',
    'sunshine',
    'slide',
    'calamity',
    'gurney',
    'adult',
    'adore',
    'weld',
    'masking',
    'print',
    'wishful',
    'foyer',
    'tofu',
    'machete',
    'diced',
    'behemoth',
    'rout',
    'midwife',
    'neglect',
    'mass',
    'game',
    'stocking',
    'folly',
    'action',
    'bubbling',
    'scented',
    'sprinter',
    'bingo',
    'egyptian',
    'comedy',
    'rung',
    'outdated',
    'radical',
    'escalate',
    'mutter',
    'desert',
    'memento',
    'kayak',
    'talon',
    'portion',
    'affirm',
    'dashing',
    'fare',
    'battle',
    'pupil',
    'rite',
    'smash',
    'true',
    'entrance',
    'counting',
    'peruse',
    'dioxide',
    'hermit',
    'carving',
    'backyard',
    'homeless',
    'medley',
    'packet',
    'tickle',
    'coming',
    'leave',
    'swing',
    'thicket',
    'reserve',
    'murder',
    'costly',
    'corduroy',
    'bump',
    'oncology',
    'swatch',
    'rundown',
    'steal',
    'teller',
    'cable',
    'oily',
    'official',
    'abyss',
    'schism',
    'failing',
    'guru',
    'trim',
    'alfalfa',
    'doubt',
    'booming',
    'bruised',
    'playful',
    'kicker',
    'jockey',
    'handmade',
    'landfall',
    'rhythm',
    'keep',
    'reassure',
    'garland',
    'sauna',
    'idiom',
    'fluent',
    'lope',
    'gland',
    'amend',
    'fashion',
    'treaty',
    'standing',
    'current',
    'sharpen',
    'cinder',
    'idealist',
    'festive',
    'frame',
    'molten',
    'sill',
    'glisten',
    'fearful',
    'basement',
    'minutia',
    'coin',
    'stick',
    'featured',
    'soot',
    'static',
    'crazed',
    'upset',
    'robotics',
    'dwarf',
    'shield',
    'butler',
    'stitch',
    'stub',
    'sabotage',
    'parlor',
    'prompt',
    'heady',
    'horn',
    'bygone',
    'rework',
    'painful',
    'composer',
    'glance',
    'acquit',
    'eagle',
    'solvent',
    'backbone',
    'smart',
    'atlas',
    'leap',
    'danger',
    'bruise',
    'seminar',
    'tinge',
    'trip',
    'narrow',
    'while',
    'jaguar',
    'seminary',
    'command',
    'cassette',
    'draw',
    'anchovy',
    'scream',
    'blush',
    'organic',
    'applause',
    'parallel',
    'trolley',
    'pathos',
    'origin',
    'hang',
    'pungent',
    'angular',
    'stubble',
    'painted',
    'forward',
    'saddle',
    'muddy',
    'orchid',
    'prudence',
    'disprove',
    'yiddish',
    'lobbying',
    'neuron',
    'tumor',
    'haitian',
    'swift',
    'mantel',
    'wardrobe',
    'consist',
    'storied',
    'extreme',
    'payback',
    'control',
    'dummy',
    'influx',
    'realtor',
    'detach',
    'flake',
    'consign',
    'adjunct',
    'stylized',
    'weep',
    'prepare',
    'pioneer',
    'tail',
    'platoon',
    'exercise',
    'dummy',
    'clap',
    'actor',
    'spark',
    'dope',
    'phrase',
    'welsh',
    'wall',
    'whine',
    'fickle',
    'wrong',
    'stamina',
    'dazed',
    'cramp',
    'filet',
    'foresee',
    'seller',
    'award',
    'mare',
    'uncover',
    'drowning',
    'ease',
    'buttery',
    'luxury',
    'bigotry',
    'muddy',
    'photon',
    'snow',
    'oppress',
    'blessed',
    'call',
    'stain',
    'amber',
    'rental',
    'nominee',
    'township',
    'adhesive',
    'lengthy',
    'swarm',
    'court',
    'baguette',
    'leper',
    'vital',
    'push',
    'digger',
    'setback',
    'accused',
    'taker',
    'genie',
    'reverse',
    'fake',
    'widowed',
    'renewed',
    'goodness',
    'featured',
    'curse',
    'shocked',
    'shove',
    'marked',
    'interact',
    'mane',
    'hawk',
    'kidnap',
    'noble',
    'proton',
    'effort',
    'patriot',
    'showcase',
    'parish',
    'mosaic',
    'coil',
    'aide',
    'breeder',
    'concoct',
    'pathway',
    'hearing',
    'bayou',
    'regimen',
    'drain',
    'bereft',
    'matte',
    'bill',
    'medal',
    'prickly',
    'sarcasm',
    'stuffy',
    'allege',
    'monopoly',
    'lighter',
    'repair',
    'worship',
    'vent',
    'hybrid',
    'buffet',
    'lively']


# Create your views here.
def home(request):
    
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,'home.html')
def button1(request):
     return render(request,'home.html')  



   
def output1(request):

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
     head.penup()
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
          if head.direction=="down":
               y=head.ycor()
               head.sety(y-20)
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
               new_segment.penup()
               segments.append(new_segment)
               delay-=0.001
               score+=10
               if score>high_score:
                    high_score=score
               pen.clear()
               pen.write("score:{} High score :{}".format(score,high_score),align="center",font=("arial",24,"bold"))  
     

          for index in range(len(segments)-1,0,-1):
               x=segments[index-1].xcor()
               y=segments[index-1].ycor()
               segments[0].goto(x,y)
          if len(segments)>0:
               x=head.xcor()
               y=head.ycor()
               segments[0].goto(x,y)
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
     wn.mainloop()     
     return render(request,'home.html')
def button2(request):
     return render(request,'button2.html')
def output2(request):
     import turtle
     import random
     # Set up the screen
     wn = turtle.Screen()
     wn.title("2048 by @TokyoEdTech")
     wn.bgcolor("black")
     wn.setup(width=450, height=400)
     wn.tracer(0)

     # Score
     score = 0

     # Grid list

     grid = [
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]

     grid_merged = [
                   [False, False, False, False],
                   [False, False, False, False],
                   [False, False, False, False],
                   [False, False, False, False]
                   ]
     # Pen
     pen.speed(0)
     pen.shape("square")
     pen.color("white")
     pen.penup()
     pen.hideturtle()
     pen.turtlesize(stretch_wid=2, stretch_len=2, outline=2)
     pen.goto(0, 260)
     def draw_grid():

          colors = {
               0: "white",
               2: "yellow",
               4: "orange",
               8: "pink",
               16: "red",
               32: "light green",
               64: "green",
               128: "light purple",
               256: "purple",
               512: "gold",
               1024: "silver",
               2048: "black"
          }
          # Top -100, 100
          grid_y = 0
          y = 120
          # Draw the grid
          for row in grid:
               grid_x = 0
               x = -120
               y -= 45
               for column in row:
                    x += 45
                    pen.goto(x, y)
            
                    # Set the color based on the value
                    value = grid[grid_y][grid_x]
                    color = colors[value]

                    pen.color(color)
                    pen.stamp()

                    pen.color("blue")
                    if column == 0:
                         number = ""
                    else:
                         number = str(column)

                    pen.sety(pen.ycor() - 10)
                    pen.write(number, align="center", font=("Courier", 14, "bold"))
                    pen.sety(pen.ycor() + 10)

                    grid_x += 1
               grid_y += 1     
     def add_random():

          added = False
          while not added:
               x = random.randint(0, 3)
               y = random.randint(0, 3)

               value = random.choice([2, 4])

               if grid[y][x] == 0:
                    grid[y][x] = value
                    added = True
     def up():
          # Go through row by row
          # Start with row 1 (note this is the index)
          for _ in range(4):
               for y in range(1, 4):
                    for x in range(0, 4):
                         # Empty
                         if grid[y-1][x] == 0:
                              grid[y-1][x] = grid[y][x]
                              grid[y][x] = 0
                              x -= 1
                              continue
                         # Same
                         if grid[y-1][x] == grid[y][x] and not grid_merged[y-1][x]:
                              grid[y-1][x] = grid[y][x] * 2
                              grid_merged[y-1][x] = True
                              grid[y][x] = 0
                              x -= 1
                              continue
          reset_grid_merged()

          print("UP")
          add_random()
          draw_grid()
     def down():
          # Go through row by row
          # Start with row 1 (note this is the index)  
          for _ in range(4):
               for y in range(2, -1, -1):
                    for x in range(0, 4):
                         # Empty
                         if grid[y+1][x] == 0:
                              grid[y+1][x] = grid[y][x]
                              grid[y][x] = 0
                              x -= 1
                              continue 
                         # Same
                         if grid[y+1][x] == grid[y][x] and not grid_merged[y+1][x]:
                              grid[y+1][x] = grid[y][x] * 2
                              grid_merged[y+1][x] = True
                              grid[y][x] = 0
                              x -= 1
                              continue 
          reset_grid_merged()

          print("DOWN")
          add_random()
          
          draw_grid()
     def reset_grid_merged():
          global grid_merged
          grid_merged = [
               [False, False, False, False],
               [False, False, False, False],
               [False, False, False, False],
               [False, False, False, False]
          ] 
     def left():
          pass
          draw_grid()  
     def right():
          pass
          draw_grid()

     draw_grid()  
     # Keyboard bindings
     wn.listen()
     wn.onkeypress(left, "Left")
     wn.onkeypress(right, "Right")
     wn.onkeypress(up, "Up")
     wn.onkeypress(down, "Down")

     wn.mainloop()                     
     return render(request,'button2.html')
   
def button3(request):
     return render(request,'button2.html')
     
def button4(request):
      return render(request,'home.html')
def output4(request):
     wn = turtle.Screen()
     wn.title("Dinosaur Game by @AYV")
     wn.bgcolor("black")
     wn.setup(height=320, width=800)
     wn.bgpic("../static/background.gif")
     wn.tracer(0)

     wn.register_shape("dinosaur.gif")
     wn.register_shape("cactus_small.gif")
     LINE_HEIGHT = -40

     pen = turtle.Turtle()
     pen.speed(0)
     pen.pensize(3)
     pen.shape("square")
     pen.color("white")
     pen.penup()

     # Draw line
     pen.goto(-400, LINE_HEIGHT)
     pen.pendown()
     pen.goto(400, LINE_HEIGHT)
     pen.penup()

     jumper = turtle.Turtle()
     jumper.speed(0)
     jumper.shape("dinosaur.gif")
     jumper.color("green")
     jumper.penup()
     jumper.dy = 0
     jumper.dx = 0
     jumper.state = "ready"
     jumper.height = 50
     jumper.width = 40
     jumper.goto(-200, LINE_HEIGHT + jumper.height/2)

     gravity = -0.8

     obstacle = turtle.Turtle()
     obstacle.speed(0)
     obstacle.shape("cactus_small.gif")
     obstacle.color("red")
     obstacle.penup()
     obstacle.dx = -3
     obstacle.height = 30
     obstacle.width = 17
     obstacle.goto(200, LINE_HEIGHT + obstacle.height/2)
     def jump():
          if jumper.state == "ready":
               jumper.dy = 12
               jumper.state = "jumping"
    
     wn.listen()
     wn.onkeypress(jump, "space")
     while True:
    # Check for landing
          if jumper.ycor() < LINE_HEIGHT + jumper.height/2:
               jumper.sety(LINE_HEIGHT + jumper.height/2)
               jumper.dy = 0
               jumper.state = "ready"

     if jumper.ycor() != LINE_HEIGHT + jumper.height/2 and jumper.state == "jumping":


         # Gravity (Affects dy)
          jumper.dy += gravity
     # Add dy to y
          y=jumper.ycor()
          y += jumper.dy
          jumper.sety(y)
    
     # Move the obstacle
          x = obstacle.xcor()
          x += obstacle.dx
          obstacle.setx(x)
    
     # Check for off the screen
     if obstacle.xcor() < -400:
               x = random.randint(400, 600)
               obstacle.setx(x)
               obstacle.dx *= 1.05
               print(obstacle.dx)
     # Check for collision
               obstacle_left = obstacle.xcor() - obstacle.width/2
               obstacle_right = obstacle.xcor() + obstacle.width/2
               obstacle_top = obstacle.ycor() + obstacle.height/2
    
               jumper_left = jumper.xcor() - jumper.width/2
               jumper_right = jumper.xcor() + jumper.width/2
               jumper_bottom = jumper.ycor() - jumper.height/2
     # 3 Conditions
     if(obstacle_left > jumper_left and obstacle_left < jumper_right and obstacle_top > jumper_bottom):
               print("GAME OVER")
               time.sleep(3)
               obstacle.goto(450, LINE_HEIGHT + obstacle.height/2)
               obstacle.dx = -3
     if(obstacle_right > jumper_left and obstacle_right < jumper_right and obstacle_top > jumper_bottom):
               print("GAME OVER")
               obstacle.goto(450, LINE_HEIGHT + obstacle.height/2)
               obstacle.dx = -3
               wn.update()

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


