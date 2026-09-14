import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def message(input):
    print(input)
message("Hello Class")

def rectangle(x):
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
rectangle(200)

def equal(x):
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal(200) 

turtle.done()