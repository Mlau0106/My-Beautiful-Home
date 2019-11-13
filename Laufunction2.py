#Laufunction2
import turtle
bob = turtle.Turtle()

def polygon(sides,distance,color):
    bob.color(color)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
def star(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.right(144)
    bob.end_fill()
def explosion(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.right(135)
        bob.end_fill()

def triangle(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(3):
        bob.forward(distance)
        bob.left(120)
    bob.end_fill()

def rectangle(sides,distance,color):
    bob.color(color)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()


        
       
        
            

