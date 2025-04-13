from turtle import Turtle, Screen
import random
from hirstcolours import hirst_colours


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

# Day 18 Project - Recreating a Hirst painting using Turtle

def line(r):
    """Takes r as an argument, draws dots in random colours r times across the x axis
    :params: r - passed in as the range for the for loop to create the line of circles
    """
    for num in range(r):
        leeroy.dot(20, hirst_colours[random.randint(0, 29)])
        leeroy.forward(50)

# making sure pen is up and speed is set to fastest
leeroy.penup()
leeroy.speed(0)

# setting starting position for x & y. Y axis will be reduced by 50 each time the programme loops
leeroy.setposition(-400.00, 300.00)
original_x = -400.00
original_y = 300.00

def make_hirst(x, y, r):
    """Takes x and y as pos arguements and r as the range for the for loop to recreate a Hirst dot painting
    :params: x - x axis for the starting position, this position will not change throughout the function
    :params: y - y axis for the starting position, this will decrease by 50 each loop
    :params: r - passed in to determine range in loop
    """
    for num in range(r):
        line(r)
        y -= 50
        leeroy.setposition(x, y)


make_hirst(original_x, original_y, 10)
screen.exitonclick()