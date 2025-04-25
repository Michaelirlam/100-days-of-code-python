from turtle import Turtle

class Paddle(Turtle):
    """Paddle class to create a paddle for the pong game."""
    def __init__(self, xpos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1) # sets size of padde to 5 units tall, 1 unit wide
        self.penup()
        self.teleport(x=xpos, y=0) # sets initial position of paddle
        
    def move_up(self):
        """Moves the paddle up by 20 units."""
        # Check if the paddle is within the upper boundary of the screen before moving up
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)

    def move_down(self):
        """Moves the paddle down by 20 units."""
        # Check if the paddle is within the lower boundary of the screen before moving down
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
    
    def computer_move(self, ball_y):
        """Move the paddle gradually toward the ball's y-coordinate."""
        if abs(self.ycor() - ball_y) > 10:  # Only move if the ball is far enough
            if self.ycor() < ball_y and self.ycor() < 240:
                self.sety(self.ycor() + 15)  # Increase speed slightly
            elif self.ycor() > ball_y and self.ycor() > -240:
                self.sety(self.ycor() - 15)

    def detect_collision(self, ball):
        """Check if the ball collides with the paddle."""
        if self.ycor() - 50 <= ball.ycor() <= self.ycor() + 50: # Check if the ball is within the paddle's vertical range
            if abs(self.xcor() - ball.xcor()) < 20: # Check if the ball is near the paddle's front edge
                return True
        return False