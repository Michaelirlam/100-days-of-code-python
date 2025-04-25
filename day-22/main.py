from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time # Import time module for sleep functionality

# Set up the screen
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# Used to track the game state
game_over = False

# Create paddles, ball, and scoreboard
paddle_one = Paddle(-580)
paddle_two = Paddle(580)
ball = Ball()
scoreboard = Scoreboard()

# Set movement for paddle one
screen.listen()
screen.onkey(paddle_one.move_up, "Up")
screen.onkey(paddle_one.move_down, "Down")

def game_loop():
    """Main game loop."""
    global game_over

    # Move the ball
    ball.move()

    # Ball-wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle two AI
    paddle_two.computer_move(ball_y=ball.ycor())

    # Ball-paddle collision
    if paddle_two.detect_collision(ball):
        ball.bounce_x()
        ball.setx(ball.xcor() - 10)  # Move ball slightly away from paddle to prevent sticking
    if paddle_one.detect_collision(ball):
        ball.bounce_x()
        ball.setx(ball.xcor() + 10) 

    # Check for out of bounds and increase score
    if ball.xcor() > 600:
        # Player scores
        scoreboard.increase_player_score()
        time.sleep(1) # Delay to allow player time after scoring
        ball.reset_position() # reset ball position and reverse direction
    elif ball.xcor() < -600:
        # Computer scores
        scoreboard.increase_computer_score()
        time.sleep(1)
        ball.reset_position()

    # Check for game over condition
    if scoreboard.player_score == 10:
        scoreboard.player_win()
        time.sleep(2)
        game_over = True
    elif scoreboard.computer_score == 10:
        scoreboard.player_lose()
        time.sleep(2)
        game_over = True
        
    # Continue the game loop if not game over
    if not game_over:
        screen.ontimer(game_loop, 16)  # Schedule the next call to game_loop, continues loop until game_over is True

# Start the game loop
game_loop()

screen.exitonclick()