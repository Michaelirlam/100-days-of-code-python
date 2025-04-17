from turtle import Turtle, Screen
import time
from snake import Snake

# Creates the initial snake using the Snake class
snake = Snake()

def close_game():
    """function for closing the game, should be used with an onkey event"""
    global game_over
    game_over = True

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Movement settings
screen.listen()
screen.onkey(close_game, "q")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game logic
game_over = False

while not game_over:
    screen.update()
    time.sleep(0.2)
    snake.move()
    


screen.bye()