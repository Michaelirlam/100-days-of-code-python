from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_over = False

def close_game():
    global game_over
    game_over = True

def left():
    snake_body[0].left(90)

def right():
    snake_body[0].right(90)

snake_body = []
for num in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setpos(x= -20 * num, y=0)
    snake_body.append(new_segment)

screen.listen()
screen.onkey(close_game, "q")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

while not game_over:
    screen.update()
    time.sleep(0.2)
    for body in range(len(snake_body) - 1, 0, -1):
        snake_body[body].goto(snake_body[body - 1].pos())
    snake_body[0].forward(20)





screen.bye()