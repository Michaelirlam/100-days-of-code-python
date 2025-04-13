from turtle import Turtle, Screen

winston = Turtle()

def move_forward():
    winston.fd(10)

def move_backward():
    winston.backward(10)

def turn_left():
    winston.left(10)

def turn_right():
    winston.right(10)

def clear():
    winston.reset()
    screen.reset()

screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")




screen.exitonclick()

