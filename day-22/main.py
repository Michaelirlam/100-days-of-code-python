from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong Game")


paddle_one = Paddle(-580)
paddle_two = Paddle(580)


screen.listen()
screen.onkey(paddle_one.move_up, "Up")
screen.onkey(paddle_one.move_down, "Down")



screen.exitonclick()