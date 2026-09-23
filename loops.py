import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.right(120)

def draw_sixty_squares(t):
    for _ in range(60):
        square(t, 100)
        t.left(5)