import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

