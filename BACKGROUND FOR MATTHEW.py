#basic shape fundamentals - practice file
import turtle
from Laufunction2 import*
turtle.colormode(255)
#turtle.bgcolor(0,0,0)
bob.width(10)
bob.speed(0)

x = -500
y = 400
jump(x,y)
for times in range(140):
    c = (25,25,times)
    bob.color(c)
    bob.forward(1000)
    jump(x,y-times*6)
bob.speed(0)
jump(-65,0)

#House base
polygon(4,200,"maroon")
triangle(200,"saddlebrown")

#Chimney
jump(-25,50)
bob.begin_fill()
bob.color(128,0,0)
for times in range(2):
    bob.forward(40)
    bob.left(90)
    bob.forward(140)
    bob.left(90)
bob.end_fill()

#Next Position for a door
jump(18,-200)

#Door
for times in range(2):
    bob.begin_fill()
    bob.color(139,69,19)
    bob.forward(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.end_fill()

#Door knob
jump(60,-153)
bob.begin_fill()
bob.color(255,255,0)
bob.circle(5)
bob.end_fill()

#Window
jump(18,-70)
bob.begin_fill()
bob.color(176,196,222)
for times in range(4):
    bob.forward(50)
    bob.left(90)
bob.end_fill()

#land
jump(-600,-150)
bob.begin_fill()
bob.color(0,128,0)
for times in range(2):
    bob.forward(525)
    bob.right(90)
    bob.forward(300)
bob.end_fill()

jump(-68,-205)
bob.right(180)
polygon(4,400,"green")

jump(600,-150)
bob.begin_fill()
bob.color(0,128,0)
bob.right(180)
for times in range(2):
    bob.forward(455)
    bob.left(90)
    bob.forward(200)
bob.end_fill()

#Moon
jump(-300,200)
bob.begin_fill()
bob.color("snow")
bob.circle(75)
bob.end_fill()

#Stars
jump(-400,200)
star(20,"snow")

jump(-150,200)
star(20,"snow")

jump(-100,300)
star(20,"snow")

jump(0,220)
star(20,"snow")

jump(100,300)
star(20,"snow")

jump(300,250)
star(20,"snow")

jump(200,370)
star(20,"snow")

jump(400,200)
star(20,"snow")

#yardwalk
jump(68,-205)
bob.right(90)
rectangle(4,50,"lightslategrey")
jump(68,-250)
rectangle(4,50,"lightslategrey")
jump(68,-295)
rectangle(4,50,"lightslategrey")
jump(68,-340)
rectangle(4,50,"lightslategrey")

#Flowers
bob.speed(0)

jump(-40,-200)
star(10,"yellow")
jump(-40,-215)
bob.color("darkgreen")
bob.forward(20)

jump(-200,-300)
star(10,"yellow")
jump(-200,-315)
bob.color("darkgreen")
bob.forward(20)

jump(-340,-220)
star(10,"yellow")
jump(-340,-235)
bob.color("darkgreen")
bob.forward(20)

jump(-400,-300)
star(10,"yellow")
jump(-400,-315)
bob.color("darkgreen")
bob.forward(20)

jump(400,-300)
star(10,"yellow")
jump(400,-315)
bob.color("darkgreen")
bob.forward(20)

jump(300,-200)
star(10,"yellow")
jump(300,-215)
bob.color("darkgreen")
bob.forward(20)

jump(200,-300)
star(10,"yellow")
jump(200,-315)
bob.color("darkgreen")
bob.forward(20)












