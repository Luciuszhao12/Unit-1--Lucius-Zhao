import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(0)


<<<<<<< HEAD
# def square(length):
#     for i in range(4):
#         t.forward(length)
#         t.left(90)

# def square(length,angle):
#     for _ in range (4):
#         t.forward(length)
#         t.right(angle)

# def drawSprial ():
#     for i in range(60):
#         square(100,90)
#         t.right(5)
# drawSprial()

# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)

# def addSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length += 25
# addSquares(5)


# def square(length,angle):
#     for i in range(4):
#         t.forward(length)
#         t.right(angle)

# def addSquares(iRange):
#     length = 5
#     for i in range(iRange):
#         square(length, 90)
#         t.right(5)
#         length += 5
# addSquares(60)
=======
def triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.right(120)

def draw_sixty_squares(t):
    for _ in range(60):
        square(t, 100)
        t.left(5)

turtle.done
>>>>>>> e9a2211d8a746e1de058413adc14ef94717e938e
