from turtle import Turtle

class Paddle(Turtle):
    """Paddle class to create a paddle for the pong game."""
    def __init__(self, xpos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1) # sets size of padde to 5 units tall, 1 unit wide
        self.penup()
        self.goto(x=xpos, y=0) # sets initial position of paddle
        
    
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
        pass