from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# This is a simple snake game using the turtle module in Python.
# The game is played using the arrow keys to control the snake's movement.
# The objective of the game is to eat the food that appears on the screen,
# which causes the snake to grow longer. The game ends if the snake collides
# with the wall or itself.
# This file is the main file that runs the game and has the game logic.

snake = Snake() # Snake class to create the snake
food = Food() # Food class to generate food at random locations
scoreboard = Scoreboard() # Scoreboard class to keep track of the score

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
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

# Game logic
game_over = False # Variable to track if the game is over
speed = 0.2 # Initial speed

while not game_over:
    screen.update()
    time.sleep(speed) # Controls the speed of the game
    snake.move() # moves the snake forward

    # checks to see if snake made contact with the food and refreshes food position and grows snake
    # score now increases when snake eats the food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh(snake_positions=snake.snake_body)
        snake.grow()
        scoreboard.increase_score()

        # Increase speed every 5 points and sets a minimum speed to avoid the game being too fast
        if scoreboard.score % 5 == 0:
            speed = max(0.05, speed - 0.02)
    
    # checks to see if snake has hit the wall and if it has, the game is over
    if snake.detect_wall_collision():
        scoreboard.game_over()
        screen.update()
        game_over = True
        

    # checks to see if snake has hit its own tail and if it has, the game is over
    if snake.detect_tail_collision():
        scoreboard.game_over()
        screen.update()
        game_over = True
    

if game_over:
    time.sleep(2) # Waits for 2 seconds before closing the game
    screen.bye() # Closes the game when the user presses "q"