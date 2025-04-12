from turtle import Turtle, Screen
import random

leeroy = Turtle()
leeroy.shape("turtle")
leeroy.color("green")
screen = Screen()
screen.colormode(255)



# challenge 1 - draw a square
def square():
    for num in range(4):
        leeroy.forward(100)
        leeroy.right(90)


# challenge 2 - draw a dashed line
def dashed_line():
    for num in range(15):
        leeroy.forward(10)
        leeroy.penup()
        leeroy.forward(10)
        leeroy.pendown()


# challenge 3 - Draw different changes from 3 - 10 sides consecutively and with different colours
def random_colour():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return leeroy.pencolor(R, G, B)

def move(loop, rt):
    random_colour()
    for num in range(loop):
        leeroy.forward(100)
        leeroy.right(rt)


def shapes():
    for num in range(3, 11):
        move(num, 360 / num)   

# challenge 4 - Random walk

def random_walk():
    leeroy.pensize(width=10)
    leeroy.speed(10)
    for num in range(500):
        
        leeroy.forward(30)
        leeroy.setheading(random.choice([0, 90, 180, 270]))

# Challenge 5 - Draw a spirograph

def spirograph(gap):
    leeroy.speed("fastest")
    for num in range(int(360 / gap)):
        random_colour()
        leeroy.circle(100)
        leeroy.left(gap)

spirograph(4)
screen.exitonclick()